import torch.nn as nn
from transformers import AutoTokenizer, AutoModel
import torch
from torch.nn import CrossEntropyLoss
import torch.nn.functional as F

class CustomClassificationHead(nn.Module):
    def __init__(self,config, num_labels):
        super(CustomClassificationHead, self).__init__()
        self.N_MSD = 5
        self.num_labels = num_labels

        # similarity feature
        config.hidden_size = 769

        self.dense = nn.Linear(config.hidden_size, config.hidden_size)
        self.batch_norm = nn.BatchNorm1d(config.hidden_size)
        self.activation = nn.ReLU()
        self.dropouts = nn.ModuleList([nn.Dropout(0.4) for _ in range(self.N_MSD)])
        self.regressor = nn.Linear(config.hidden_size, self.num_labels)
    
    def forward(self, features, **kwargs):
        # featuresの形状は [batch_size, sequence_length, hidden_size] を想定
        batch_size, hidden_size = features.size()

        # featuresを [batch_size, hidden_size] に変形
        features = features.view(batch_size, -1, hidden_size).mean(dim=1)

        # 線形変換とドロップアウトを適用
        features = self.dense(features)
        features = self.batch_norm(features)
        features = self.activation(features)
        logits = sum([self.regressor(dropout(features)) for dropout in self.dropouts]) / self.N_MSD
        return logits

class CustomBertModel(nn.Module):
    def __init__(self, loss_ratio=0.5, sub_loss_ratio=0.5, alpha=0.5, beta=0.8):
        super(CustomBertModel, self).__init__()
        self.model = AutoModel.from_pretrained("microsoft/codebert-base")
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
    
    def forward(self, input_ids=None, attention_mask=None, labels=None, sub_labels=None, perturbed_input_ids=None, perturbed_attention_mask=None):
        
        f_input_ids = input_ids.float()
        f_perturbed_input_ids = perturbed_input_ids.float()
        cosine_sim = F.cosine_similarity(f_input_ids, f_perturbed_input_ids, dim=-1)
        similarity_feature = cosine_sim.unsqueeze(-1)

        outputs = self.model(input_ids, attention_mask=attention_mask)
        pooled_output = pooled = outputs[1]
        pooled_output = self.dropout(pooled_output)
        similarity_feature = similarity_feature * 1.0
        new_pooled_output = torch.cat([pooled_output, similarity_feature], dim=-1)
        #sub_logits = self.id_classifier(pooled_output)

        loss = None
        cos_loss = None
        similarity_feature = None
        #similarity_loss = None
        if labels is not None:
            dist = ((pooled.unsqueeze(1) - pooled.unsqueeze(0)) ** 2).mean(-1)
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

            """
            if sub_labels is not None:
                sub_loss_fct = CrossEntropyLoss()
                sub_loss = sub_loss_fct(sub_logits.view(-1, self.num_id_labels), sub_labels.view(-1))
                loss += sub_loss * self.sub_loss_ratio
            """
        else:
            logits = self.classifier(new_pooled_output)

        output = (logits,) + outputs[2:]
        output = output + (pooled,)
        return ((loss, cos_loss) + output) if loss is not None else output


