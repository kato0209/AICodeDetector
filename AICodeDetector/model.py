import torch.nn as nn
from transformers import AutoTokenizer, AutoModel,AutoModelForSeq2SeqLM
import torch
from torch.nn import CrossEntropyLoss
import torch.nn.functional as F
from sentence_transformers import SentenceTransformer, util
from pertube_data import pertubate_code
import re

from pertubate import rewrite_code

class CustomClassificationHead(nn.Module):
    def __init__(self,config, num_labels):
        super(CustomClassificationHead, self).__init__()
        self.N_MSD = 5
        self.num_labels = num_labels

        # similarity feature
        config.hidden_size = 768 + 768
        hidden_size2 = 768
        hidden_size3 = 512

        self.dense = nn.Linear(config.hidden_size, hidden_size2)
        self.dense2 = nn.Linear(hidden_size2, hidden_size3)
        self.batch_norm = nn.BatchNorm1d(hidden_size2)
        self.activation = nn.ReLU()
        self.dropouts = nn.ModuleList([nn.Dropout(0.4) for _ in range(self.N_MSD)])
        self.regressor = nn.Linear(hidden_size3, self.num_labels)
    
    def forward(self, features, **kwargs):
        # featuresの形状は [batch_size, sequence_length, hidden_size] を想定
        batch_size, hidden_size = features.size()

        # featuresを [batch_size, hidden_size] に変形
        features = features.view(batch_size, -1, hidden_size).mean(dim=1)

        # 線形変換とドロップアウトを適用
        features = self.dense(features)
        features = self.batch_norm(features)
        features = self.activation(features)
        features = self.dense2(features)

        logits = sum([self.regressor(dropout(features)) for dropout in self.dropouts]) / self.N_MSD
        return logits

class CustomBertModel(nn.Module):
    def __init__(self, loss_ratio=0.5, sub_loss_ratio=0.5, alpha=0.5, beta=0.8):
        super(CustomBertModel, self).__init__()
        self.model = AutoModel.from_pretrained("microsoft/codebert-base")
        self.sentence_model = SentenceTransformer('Sakil/sentence_similarity_semantic_search')
        self.dropout = nn.Dropout(self.model.config.hidden_dropout_prob)
        self.classifier = CustomClassificationHead(self.model.config, num_labels=2)
        #self.id_classifier = CustomClassificationHead(self.model.config, num_labels=7)
        self.num_labels = 2
        self.num_id_labels = 7
        #self.alpha = 0.1
        self.loss_ratio = loss_ratio
        self.alpha = alpha
        self.beta = beta
        self.sub_loss_ratio = sub_loss_ratio
        
    
    def return_model(self):
        return self.model
    
    def forward(self, input_ids=None, attention_mask=None, labels=None, original_code=None, perturb_code=None):
        
        sentences = []
        for code in original_code:
            sentences.append(code)
        for code in perturb_code:
            sentences.append(code)
        embedings = self.sentence_model.encode(sentences)
        cos_sim = util.cos_sim(embedings, embedings)
        similarity_scores = [cos_sim[i, len(original_code) + i] for i in range(len(original_code))]
        similarity_scores = torch.tensor(similarity_scores).view(-1, 1).to(input_ids.device)
        #similarity_scoresを[size, 1]から[size, 768]に変換
        similarity_scores = similarity_scores.repeat(1, 768)

        outputs = self.model(input_ids, attention_mask=attention_mask)
        pooled_output = pooled = outputs[1]
        pooled_output = self.dropout(pooled_output)
        new_pooled_output = torch.cat([pooled_output, similarity_scores], dim=-1)

        loss = None
        cos_loss = None
        if labels is not None:
            dist = ((new_pooled_output.unsqueeze(1) - new_pooled_output.unsqueeze(0)) ** 2).mean(-1)
            mask = (labels.unsqueeze(1) == labels.unsqueeze(0)).float()
            mask = mask - torch.diag(torch.diag(mask))
            neg_mask = (labels.unsqueeze(1) != labels.unsqueeze(0)).float()
            max_dist = (dist * mask).max()
            cos_loss = (dist * mask).sum(-1) / (mask.sum(-1) + 1e-3) + (F.relu(max_dist - dist) * neg_mask).sum(-1) / (neg_mask.sum(-1) + 1e-3)
            cos_loss = cos_loss.mean()

            loss_fct = CrossEntropyLoss()

            logits = self.classifier(new_pooled_output)
            loss = loss_fct(logits.view(-1, self.num_labels), labels.view(-1))
            loss = self.loss_ratio * loss + self.alpha * cos_loss
        else:
            logits = self.classifier(new_pooled_output)

        output = (logits,) + outputs[2:]
        output = output + (pooled,)
        return ((loss, cos_loss) + output) if loss is not None else output


class CustomCodeLlamaModel(nn.Module):
    def __init__(self, model, tokenizer, sentence_model):
        super(CustomCodeLlamaModel, self).__init__()
        self.model = model
        self.tokenizer = tokenizer
        self.sentence_model = sentence_model
    
    def rewrite_code(self, codes, model_config, args):
        prompt = """
        Generate the following Python code rewrite according to your idea.
        Please do not output anything other than the rewritten Python code.
        ```
        {code}
        ```
        """

        tokenizer = model_config['tokenizer']
        model = model_config['model']

        # [batch_size, token_length]の配列を用意
        y = [[0 for _ in range(args.token_length)] for _ in range(args.batch_size)]
        state = [[0 for _ in range(args.token_length)] for _ in range(args.batch_size)]
        

        rewrite_codes = []
        i = 0
        for code in codes:
            input_prompt = prompt.format(code=code)
            input_ids = tokenizer(input_prompt, return_tensors="pt", truncation=True, max_length=128).input_ids
            input_ids = input_ids.to(args.DEVICE)
            
            # トークンごとの生成を開始
            output_ids = input_ids
            output_sentences = []
            j = 0
            for _ in range(128):  # 生成を128トークンに制限
                outputs = model.generate(output_ids, do_sample=True, max_length=output_ids.size(-1) + 1, 
                                        top_p=0.95, temperature=0.2, pad_token_id=tokenizer.pad_token_id, use_cache=True)
                y[i][j] = outputs[:, -1].unsqueeze(-1)
                state[i][j] = output_ids
                output_ids = torch.cat([output_ids, outputs[:, -1].unsqueeze(-1)], dim=-1)
                if output_ids[0, -1] == tokenizer.eos_token_id:
                    break
                j += 1
            # y[i]を結合してoutput_sentenceを作成
            output_sentence = tokenizer.decode(torch.cat(y[i], dim=-1)[0], skip_special_tokens=True)
            rewrite_codes.append(output_sentence)
            i += 1
        
        return rewrite_codes, y, state

    def forward(self, original_codes=None, labels=None, args=None, model_config=None):
        #_, perturbed_codes = pertubate_code(original_codes, model_config, args)
        perturbed_codes, y, state = self.rewrite_code(original_codes, model_config, args)

        sentences = []
        for code in original_codes:
            sentences.append(code)
        for code in perturbed_codes:
            sentences.append(code)
        embedings = self.sentence_model.encode(sentences)
        cos_sim = util.cos_sim(embedings, embedings).requires_grad_(True)
        # original_codesとperturbed_codesのcos類似度を取得
        similarity_scores = [cos_sim[i, len(original_codes) + i] for i in range(len(original_codes))]
        similarity_scores = torch.tensor(similarity_scores).view(-1, 1).to(self.model.device).requires_grad_(True)
        
        ai_similarity = []
        human_similarity = []
        for i in range(len(similarity_scores)):
            if labels[i] == 1:
                ai_similarity.append(similarity_scores[i])
            else:
                human_similarity.append(similarity_scores[i])
        ai_similarity = torch.tensor(ai_similarity).view(-1, 1).to(self.model.device)
        human_similarity = torch.tensor(human_similarity).view(-1, 1).to(self.model.device)

        #similarity_scoresの平均をベースラインに
        loss = 0.0
        for n in range(args.batch_size):
            for t in range(args.token_length):
                outputs = self.model(input_ids=state[n][t])
                logits = outputs.logits

                # 入力シーケンスの最後のトークンに対するロジットを抽出
                last_token_logits = logits[0, -1, :]
                # ログ確率を計算
                log_probs = F.log_softmax(last_token_logits, dim=-1)
                target_token_log_prob = log_probs[y[n][t].item()]

                if labels[n] == 1:
                    baseline = torch.mean(ai_similarity)
                    reward = similarity_scores[n].item()
                    R = reward - baseline
                else:
                    baseline = 1 - torch.mean(human_similarity)
                    reward = 1 - similarity_scores[n].item()
                    R = (reward - baseline) * 0.5
                loss += -target_token_log_prob * R
        loss /= args.batch_size * args.token_length

        return loss, similarity_scores
