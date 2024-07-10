from loguru import logger
from tqdm import tqdm

from masking import tokenize_and_mask
from preprocessing import preprocess_and_save
from load_model import load_mask_filling_model, load_model
from filling_mask import replace_masks
from extract_fill import extract_fills, apply_extracted_fills
from code_dataset import CodeDataset, CodeDatasetFromCodeSearchNet, CodeDatasetForLLM
import argparse
import torch
import os
import datetime
from torch.utils.data import DataLoader, random_split

from model import CustomBertModel, CustomCodeLlamaModel, SimilarityModel
from pertubate import rewrite_code
from transformers.optimization import AdamW, get_linear_schedule_with_warmup
from utils.model_save import model_save
from utils.confusion_matrix import plot_confusion_matrix
from utils.generate_cs_data import generate_data
from pertube_data import pertube_data

from sklearn.metrics import accuracy_score, roc_auc_score, roc_curve, auc, f1_score
from datetime import datetime
import random
import logging
from sklearn.metrics import classification_report, confusion_matrix

import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

from transformers import AutoTokenizer, AutoModel,AutoModelForSeq2SeqLM
from sentence_transformers import SentenceTransformer, util

parser = argparse.ArgumentParser()
parser.add_argument('--dataset', type=str, default="writing")
parser.add_argument('--dataset_key', type=str, default="document")
parser.add_argument('--pct_words_masked', type=float, default=0.3)
parser.add_argument('--span_length', type=int, default=2)
parser.add_argument('--n_samples', type=int, default=5)
parser.add_argument('--n_perturbation_list', type=str, default="10")
parser.add_argument('--n_perturbation_rounds', type=int, default=1)
parser.add_argument('--base_model_name', type=str, default="")
parser.add_argument('--scoring_model_name', type=str, default="")
parser.add_argument('--mask_filling_model_name', type=str, default="Salesforce/CodeT5-large")
parser.add_argument('--batch_size', type=int, default=64)
parser.add_argument('--token_length', type=int, default=128)
parser.add_argument('--chunk_size', type=int, default=20)
parser.add_argument('--n_similarity_samples', type=int, default=20)
parser.add_argument('--int8', action='store_true')
parser.add_argument('--half', action='store_true')
parser.add_argument('--base_half', action='store_true')
parser.add_argument('--do_top_k', action='store_true')
parser.add_argument('--top_k', type=int, default=40)
parser.add_argument('--do_top_p', action='store_true')
parser.add_argument('--top_p', type=float, default=0.96)
parser.add_argument('--output_name', type=str, default="test_ipynb")
parser.add_argument('--openai_model', type=str, default=None)
parser.add_argument('--openai_key', type=str)
parser.add_argument('--DEVICE', type=str, default='cuda')
parser.add_argument('--buffer_size', type=int, default=1)
parser.add_argument('--mask_top_p', type=float, default=1.0)
parser.add_argument('--mask_temperature', type=float, default=1.0)
parser.add_argument('--pre_perturb_pct', type=float, default=0.0)
parser.add_argument('--pre_perturb_span_length', type=int, default=5)
parser.add_argument('--random_fills', action='store_true')
parser.add_argument('--random_fills_tokens', action='store_true')
parser.add_argument('--cache_dir', type=str, default="~/.cache/huggingface/hub")
parser.add_argument('--prompt_len', type=int, default=30)
parser.add_argument('--generation_len', type=int, default=200)
parser.add_argument('--min_words', type=int, default=55)
parser.add_argument('--temperature', type=float, default=1)
parser.add_argument('--baselines', type=str, default="LRR,DetectGPT,NPR")
parser.add_argument('--perturb_type', type=str, default="random")
parser.add_argument('--pct_identifiers_masked', type=float, default=0.5)
parser.add_argument('--min_len', type=int, default=0)
parser.add_argument('--max_len', type=int, default=128)
parser.add_argument('--max_comment_num', type=int, default=10)
parser.add_argument('--max_def_num', type=int, default=5)
parser.add_argument('--cut_def', action='store_true')
parser.add_argument('--max_todo_num', type=int, default=3)
parser.add_argument("--learning_rate", default=1e-5, type=float)
parser.add_argument("--adam_epsilon", default=1e-6, type=float)
parser.add_argument("--num_train_epochs", default=5, type=float)
parser.add_argument("--warmup_ratio", default=0.01, type=float)
parser.add_argument("--weight_decay", default=0.06, type=float)

args_dict = {
    'dataset': "TheVault",
    # 'dataset': "CodeSearchNet",
    'dataset_key': "CodeLlama-7b-hf-10000-tp0.2",
    # 'dataset_key': "CodeLlama-7b-hf-10000-tp1.0",
    'pct_words_masked': 0.5,
    'pct_identifiers_masked': 0.75,
    'span_length': 2,
    'n_samples': 500,
    'n_perturbation_list': "50",
    'n_perturbation_rounds': 1,
    #'base_model_name': "codellama/CodeLlama-7b-hf",
    #'base_model_name': "codellama/CodeLlama-13b-Python-hf",
    'base_model_name': "meta-llama/CodeLlama-7b-Python-hf",
    'mask_filling_model_name': "Salesforce/codet5p-770m",
    'batch_size': 4,
    'chunk_size': 10,
    'n_similarity_samples': 20,
    'int8': False,
    'half': False,
    'base_half': False,
    'do_top_k': False,
    'top_k': 40,
    'do_top_p': False,
    'top_p': 0.96,
    'output_name': "test_ipynb",
    'openai_model': None,
    'openai_key': None,
    'buffer_size': 1,
    'mask_top_p': 1.0,
    'mask_temperature': 1,
    'pre_perturb_pct': 0.0,
    'pre_perturb_span_length': 5,
    'random_fills': False,
    'random_fills_tokens': False,
    'cache_dir': "~/.cache/huggingface/hub",
    'prompt_len': 30,
    'generation_len': 200,
    'min_words': 55,
    'temperature': 1,
    'baselines': "LRR,DetectGPT,NPR",
    'perturb_type': "random-insert-space+newline",
    'min_len': 0,
    'max_len': 128,
    'max_comment_num': 10,
    'max_def_num': 5,
    'cut_def': False,
    'max_todo_num': 3
}

input_args = []
for key, value in args_dict.items():
    if value:
        input_args.append(f"--{key}={value}")

args = parser.parse_args(input_args)

device = args.DEVICE

#def generate_data(max_num=1000, min_len=0, max_len=128, max_comment_num=10, max_def_num=5, cut_def=False, max_todo_num=3, path=None):
#
#    logger.info(f'Loading data from {path}')
#    import json
#    all_originals = []
#    all_samples = []  # machine generated
#
#    max_def_num_count = 0
#    min_len_count = 0
#    max_comment_num_count = 0
#    function_comment_num_count = 0
#    max_todo_num_count = 0
#
#    with open(path, 'r') as f:
#        for line in tqdm(f, ncols=70):
#            line = line.strip()
#            if line == '':
#                continue
#            line = json.loads(line)
#
#            # cut out the 'def' part after the first generation
#            if cut_def:
#                line['output'] = line['output'].split('def')[0]
#                line['solution'] = line['solution'].split('def')[0]
#
#            # I don't like there to have too many 'def' in the code
#            # ~100/100000 examples have more than 3 'def'
#            if line['solution'].count('def') > max_def_num or line['output'].count('def') > max_def_num:
#                max_def_num_count += 1
#                continue
#
#            # avoid examples that are too short (less than min_len words)
#            # around 2000/100000 examples have around 55 words
#            if len(line['solution'].split()) < min_len or len(line['output'].split()) < min_len:
#                min_len_count += 1
#                continue
#
#            # if the are too many comments, skip
#            def count_comment(text):
#                return text.count('#')
#
#            if count_comment(line['solution']) > max_comment_num or count_comment(line['output']) > max_comment_num:
#                max_comment_num_count += 1
#                continue
#
#            # if there are too many TODOs, skip
#            def count_todo_comment(text):
#                return text.count('# TODO') + text.count('# todo')
#
#            if count_todo_comment(line['solution']) > max_todo_num or count_todo_comment(line['output']) > max_todo_num:
#                max_todo_num_count += 1
#                continue
#
#            # the number of text.count("'''") and text.count('"""') should be <1
#            if line['solution'].count("'''") > 0 or line['solution'].count('"""') > 0 or line['output'].count("'''") > 0 or line['output'].count('"""') > 0:
#                function_comment_num_count += 1
#                continue
#
#            # cut to 128 tokens
#            all_originals.append(' '.join(line['solution'].split(' ')[:max_len]))
#            all_samples.append(' '.join(line['output'].split(' ')[:max_len]))
#
#    logger.info(f'{max_def_num_count} examples have more than {max_def_num} "def"')
#    logger.info(f'{min_len_count} examples have less than {min_len} words')
#    logger.info(f'{max_comment_num_count} examples have more than {max_comment_num} comments')
#    logger.info(f'{max_todo_num_count} examples have more than {max_todo_num} TODOs')
#    logger.info(f'{function_comment_num_count} examples have more than 1 function comment')
#    logger.info(f'Loaded {len(all_originals)} examples after filtering, and will return {min(max_num, len(all_originals))} examples')
#
#    # statistical analysis
#    # import random
#    # random.seed(42)
#    # random.shuffle(all_originals)
#    # random.shuffle(all_samples)
#    
#    #all_samples = random.sample(all_samples, 800)
#    all_samples = random.sample(all_samples, 70)
#
#    data = {
#        "original": all_originals,
#        "sampled": all_samples
#    }
#
#    return data

datasets_paths = [
    "CodeSearchNetDatasets/outputs_incoder_0.2.txt",
    "CodeSearchNetDatasets/outputs_phi1_0.2.txt",
    "CodeSearchNetDatasets/outputs_starcoder_0.2.txt",
    "CodeSearchNetDatasets/outputs_wizardcoder_0.2.txt",
    "CodeSearchNetDatasets/outputs_codegen2_0.2.txt",
    "CodeSearchNetDatasets/outputs_Llama_0.2.txt",
    "CodeSearchNetDatasets/outputs_incoder_1.0.txt",
    "CodeSearchNetDatasets/outputs_phi1_1.0.txt",
    "CodeSearchNetDatasets/outputs_starcoder_1.0.txt",
    "CodeSearchNetDatasets/outputs_wizardcoder_1.0.txt",
    "CodeSearchNetDatasets/outputs_codegen2_1.0.txt",
    "CodeSearchNetDatasets/outputs_Llama_1.0.txt",
]

data = {
    "original": [],
    "sampled": []
}
i = 0
for path in datasets_paths:
    sep_data = generate_data(path=path)
    data["original"] = data["original"] + sep_data["original"]

    data["sampled"] = data["sampled"] + sep_data["sampled"]
    i += 1

data["original"] = list(set(data["original"]))
data["sampled"] = list(set(data["sampled"]))

# dataを800件に originalはランダムに抽出
data["original"] = random.sample(data["original"], 800)
data["sampled"] = data["sampled"][:800]

train_data = {
    "original": data["original"][:int(len(data["original"])*0.7)],
    "sampled": data["sampled"][:int(len(data["sampled"])*0.7)]
}

val_data = {
    "original": data["original"][int(len(data["original"])*0.7):int(len(data["original"])*0.8)],
    "sampled": data["sampled"][int(len(data["sampled"])*0.7):int(len(data["sampled"])*0.8)]
}

test_data = {
    "original": data["original"][int(len(data["original"])*0.8):],
    "sampled": data["sampled"][int(len(data["sampled"])*0.8):]
}

"""
data_num = 32
# train_dataを先頭の10件に
train_data["original"] = train_data["original"][:data_num]
train_data["sampled"] = train_data["sampled"][:data_num]

# val_dataを先頭の10件に
val_data["original"] = val_data["original"][:data_num]
val_data["sampled"] = val_data["sampled"][:data_num]

# test_dataを先頭の10件に
test_data["original"] = test_data["original"][:data_num]
test_data["sampled"] = test_data["sampled"][:data_num]
"""

#train_data = pertube_data(train_data, model_config=model_config, args=args)
#val_data = pertube_data(val_data, model_config=model_config, args=args)
#test_data = pertube_data(test_data, model_config=model_config, args=args)
train_dataset = CodeDatasetForLLM(train_data)
val_dataset = CodeDatasetForLLM(val_data)
test_dataset = CodeDatasetForLLM(test_data)

train_dataloader = DataLoader(train_dataset, args.batch_size, shuffle=True)
validation_dataloader = DataLoader(val_dataset, args.batch_size, shuffle=False)
test_dataloader = DataLoader(test_dataset, args.batch_size, shuffle=False)

model_config = {}
model_config = load_model(args, args.base_model_name, model_config)
sm = SimilarityModel(model=model_config['sentence_model'], tokenizer=model_config['sentence_model_tokenizer'])
#model_path = 'saved_model/model_sm_20240628_064206.pth' 
model_path = 'saved_model/model_sm_20240630_120305.pth' 
sm.load_state_dict(torch.load(model_path, map_location=device))
sm.to(device)

cclm = CustomCodeLlamaModel(model=model_config['model'], tokenizer=model_config['tokenizer'], sentence_model=sm, sentence_model_tokenizer=model_config['sentence_model_tokenizer'])
cclm.to(device)

selected_params = [
    # 初期層
    "model.embed_tokens.weight",

    # 第1層の全パラメータ
    "model.layers.0.self_attn.q_proj.weight",
    "model.layers.0.self_attn.k_proj.weight",
    "model.layers.0.self_attn.v_proj.weight",
    "model.layers.0.self_attn.o_proj.weight",
    "model.layers.0.mlp.gate_proj.weight",
    "model.layers.0.mlp.up_proj.weight",
    "model.layers.0.mlp.down_proj.weight",
    "model.layers.0.input_layernorm.weight",
    "model.layers.0.post_attention_layernorm.weight",

    # 中間層の一部
    "model.layers.10.self_attn.q_proj.weight",
    "model.layers.10.self_attn.k_proj.weight",
    "model.layers.10.self_attn.v_proj.weight",
    "model.layers.10.self_attn.o_proj.weight",
    "model.layers.10.mlp.gate_proj.weight",
    "model.layers.10.mlp.up_proj.weight",
    "model.layers.10.mlp.down_proj.weight",
    "model.layers.10.input_layernorm.weight",
    "model.layers.10.post_attention_layernorm.weight",

    "model.layers.20.self_attn.q_proj.weight",
    "model.layers.20.self_attn.k_proj.weight",
    "model.layers.20.self_attn.v_proj.weight",
    "model.layers.20.self_attn.o_proj.weight",
    "model.layers.20.mlp.gate_proj.weight",
    "model.layers.20.mlp.up_proj.weight",
    "model.layers.20.mlp.down_proj.weight",
    "model.layers.20.input_layernorm.weight",
    "model.layers.20.post_attention_layernorm.weight",

    # 最終層
    "model.layers.31.self_attn.q_proj.weight",
    "model.layers.31.self_attn.k_proj.weight",
    "model.layers.31.self_attn.v_proj.weight",
    "model.layers.31.self_attn.o_proj.weight",
    "model.layers.31.mlp.gate_proj.weight",
    "model.layers.31.mlp.up_proj.weight",
    "model.layers.31.mlp.down_proj.weight",
    "model.layers.31.input_layernorm.weight",
    "model.layers.31.post_attention_layernorm.weight",

    # 正規化層と出力層
    "model.norm.weight",
    "lm_head.weight"
]

# すべてのパラメータをループして、必要なものを浮動小数点に変換する
for name, param in cclm.model.named_parameters():
    if name in selected_params:
        param.requires_grad = True
    else:
        param.requires_grad = False


total_steps = int(len(train_dataloader) * args.num_train_epochs)
warmup_steps = int(total_steps * args.warmup_ratio)

base_lr = args.learning_rate

optimizer_parameters = []
no_decay = ["LayerNorm.weight", "bias"]

"""
# デコーダー部分のパラメータだけを学習可能に設定
for name, param in cclm.model.named_parameters():
    if 'decoder' in name:
        param.requires_grad = True
    else:
        param.requires_grad = False
"""

# 正則化を適用しないパラメータ
optimizer_parameters.append({
    'params': [
        p for n, p in cclm.model.named_parameters()
        if any(nd in n for nd in no_decay)
    ],
    'weight_decay': 0.0,
    'lr': base_lr
})


optimizer = AdamW(optimizer_parameters, lr=args.learning_rate, eps=args.adam_epsilon)
scheduler = get_linear_schedule_with_warmup(optimizer, num_warmup_steps=warmup_steps, num_training_steps=total_steps)

# Initialize lists to store loss values
train_loss_values = []
validation_loss_values = []

cclm.train()
num_steps = 0
for epoch in range(int(args.num_train_epochs)):
    train_loss = 0.0
    for batch in train_dataloader:
        codes = batch['code']
        labels = batch['labels'].to(device)
        outputs = cclm(original_codes=codes, labels=labels, model_config=model_config, args=args)
        
        loss, _ = outputs[0], outputs[1]
        loss.backward()
        optimizer.step()
        scheduler.step()
        cclm.zero_grad()

        train_loss += loss.item()
        num_steps += 1

    train_loss /= len(train_dataloader)
    train_loss_values.append(train_loss)
    print(f"Epoch: {epoch}, Training Loss: {train_loss}")

    cclm.eval()
    validation_loss = 0.0
    with torch.no_grad():
        for batch in validation_dataloader:
            codes = batch['code']
            labels = batch['labels'].to(device)
            outputs = cclm(original_codes=codes, labels=labels, model_config=model_config, args=args)
            loss, _  = outputs[0], outputs[1]
            validation_loss += loss.item()

    validation_loss /= len(validation_dataloader)
    validation_loss_values.append(validation_loss)
    print(f"Validation Loss after epoch {epoch}: {validation_loss}")
    cclm.train()

model_save(cclm)
print("done training")
# Plot the learning curve
plt.figure(figsize=(12, 6))

plt.plot(train_loss_values, label="Training Loss")
plt.plot(validation_loss_values, label="Validation Loss")

plt.xlabel("Training Steps")
plt.ylabel("Loss")
plt.title("Learning Curve")
plt.legend()
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
plt.savefig(f"./learning_result/learning_curve_{timestamp}.png")

# Test the model and print out the confusion matrix
log_path = './logs'
os.makedirs(log_path, exist_ok=True)
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
logging.basicConfig(filename=os.path.join(log_path, f'test_{timestamp}.log'),
                    force=True,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)

cclm.eval()
label_list, pred_list, all_similarities, all_labels = [], [], [], []
with torch.no_grad():
    for batch in test_dataloader:
        codes = batch['code']
        labels = batch['labels'].to(device)
        outputs = cclm(original_codes=codes, labels=labels, model_config=model_config, args=args)
        loss, similarities = outputs[0], outputs[1]
        
        similarities = similarities.detach().cpu().numpy()
        labels = labels.detach().cpu().numpy()
        
        all_similarities.extend(similarities)
        all_labels.extend(labels)
        
        for i in range(len(similarities)):
            if similarities[i] > 0.3:
                pred = 1
            else:
                pred = 0
            pred_list.append(pred)
        label_list += labels.tolist()

# Convert lists to numpy arrays
all_similarities = np.array(all_similarities)
all_labels = np.array(all_labels)

# ROC curve based threshold
fpr, tpr, thresholds = roc_curve(all_labels, all_similarities)
J = tpr - fpr
ix = np.argmax(J)
best_threshold_roc = thresholds[ix]
print('Best Threshold based on ROC curve=%f' % (best_threshold_roc))

# F1 score based threshold
best_f1 = 0
best_threshold_f1 = 0
for threshold in thresholds:
    preds = (all_similarities >= threshold).astype(int)
    f1 = f1_score(all_labels, preds)
    if f1 > best_f1:
        best_f1 = f1
        best_threshold_f1 = threshold

print('Best Threshold based on F1=%f with F1=%f' % (best_threshold_f1, best_f1))

accuracy = accuracy_score(label_list, pred_list)
print(label_list)
print(pred_list)
print(accuracy)

auc = roc_auc_score(label_list, pred_list)
print(f"ROC AUC : {auc}")

# threthfold score
pred_list = []
for i in range(len(all_similarities)):
    if all_similarities[i] > best_threshold_roc:
        pred = 1
    else:
        pred = 0
    pred_list.append(pred)

accuracy = accuracy_score(label_list, pred_list)
print(label_list)
print(pred_list)
print(accuracy)
auc = roc_auc_score(label_list, pred_list)
print(f"ROC AUC Threshold : {auc}")

target_names = ['Human','ChatGPT']
logging.info('Confusion Matrix')
cm = confusion_matrix(label_list, pred_list)
plot_confusion_matrix(cm, target_names, title='Confusion Matrix')
logging.info('Classification Report')
logging.info(classification_report(label_list, pred_list, target_names=target_names))
