from loguru import logger
from tqdm import tqdm

from masking import tokenize_and_mask
from preprocessing import preprocess_and_save
from load_model import load_mask_filling_model, load_model
from filling_mask import replace_masks
from extract_fill import extract_fills, apply_extracted_fills
from code_dataset import CodeDataset, CodeDatasetFromCodeSearchNet, CodeDatasetForLLM, CodeDatasetRewriting
import argparse
import torch
import os
import datetime
from torch.utils.data import DataLoader, random_split

from model import CustomBertModel, CustomCodeLlamaModel, SimilarityModel
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

from peft import get_peft_model, LoraConfig, TaskType, prepare_model_for_kbit_training

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
parser.add_argument("--num_train_epochs", default=3, type=float)
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
    'base_model_name': "codellama/CodeLlama-13b-Instruct-hf",
    #'base_model_name': "meta-llama/CodeLlama-7b-Python-hf",
    #'base_model_name': "meta-llama/Meta-Llama-3-8B-Instruct",
    'mask_filling_model_name': "Salesforce/codet5p-770m",
    'batch_size': 16,
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

from utils.download_data import download_data_from_json
ai_data = download_data_from_json('rewrite_dataset/rewrite_codellama_AI_origin_codellama.json')
human_data = download_data_from_json('rewrite_dataset/rewrite_codellama_Human_origin_codellama.json')

#from util_func import remove_comments
#
#human_data["original"] = [remove_comments(code) for code in human_data["original"]]
#human_data["rewrite"] = [remove_comments(code) for code in human_data["rewrite"]]
#
#ai_data["original"] = [remove_comments(code) for code in ai_data["original"]]
#ai_data["rewrite"] = [remove_comments(code) for code in ai_data["rewrite"]]

data = {
    "human": human_data,
    "ai": ai_data
}

human_train_data = {
    "original": data["human"]["original"][:int(len(data["human"]["original"])*0.7)],
    "rewrite": data["human"]["rewrite"][:int(len(data["human"]["rewrite"])*0.7)]
}
ai_train_data = {
    "original": data["ai"]["original"][:int(len(data["ai"]["original"])*0.7)],
    "rewrite": data["ai"]["rewrite"][:int(len(data["ai"]["rewrite"])*0.7)]
}

train_data = {
    "human": human_train_data,
    "ai": ai_train_data
}

human_val_data = {
    "original": data["human"]["original"][int(len(data["human"]["original"])*0.7):int(len(data["human"]["original"])*0.8)],
    "rewrite": data["human"]["rewrite"][int(len(data["human"]["rewrite"])*0.7):int(len(data["human"]["rewrite"])*0.8)]
}
ai_val_data = {
    "original": data["ai"]["original"][int(len(data["ai"]["original"])*0.7):int(len(data["ai"]["original"])*0.8)],
    "rewrite": data["ai"]["rewrite"][int(len(data["ai"]["rewrite"])*0.7):int(len(data["ai"]["rewrite"])*0.8)]
}
val_data = {
    "human": human_val_data,
    "ai": ai_val_data
}

human_test_data = {
    "original": data["human"]["original"][int(len(data["human"]["original"])*0.8):],
    "rewrite": data["human"]["rewrite"][int(len(data["human"]["rewrite"])*0.8):]
}
ai_test_data = {
    "original": data["ai"]["original"][int(len(data["ai"]["original"])*0.8):],
    "rewrite": data["ai"]["rewrite"][int(len(data["ai"]["rewrite"])*0.8):]
}
test_data = {
    "human": human_test_data,
    "ai": ai_test_data
}

model_config = {}
model_config = load_model(args, args.base_model_name, model_config)

train_dataset = CodeDatasetRewriting(train_data, model_config, args)
val_dataset = CodeDatasetRewriting(val_data, model_config, args)
test_dataset = CodeDatasetRewriting(test_data, model_config, args)

train_dataloader = DataLoader(train_dataset, args.batch_size, shuffle=True)
validation_dataloader = DataLoader(val_dataset, args.batch_size, shuffle=False)
test_dataloader = DataLoader(test_dataset, args.batch_size, shuffle=False)

sm = SimilarityModel(model=model_config['sentence_model'], tokenizer=model_config['sentence_model_tokenizer'])
model_path = 'saved_model/model_sm_20240628_064206.pth' 
#model_path = 'saved_model/model_sm_20240630_120305.pth' 
sm.load_state_dict(torch.load(model_path, map_location=device))
sm.to(device)

model_config['model'] = prepare_model_for_kbit_training(model_config['model'])

lora_config = LoraConfig(
    r=8,
    lora_alpha=32,
    target_modules=[
        "q_proj",
        "k_proj",
        "v_proj",
        "o_proj",
    ],
    lora_dropout=0.05,
    bias="none",
    fan_in_fan_out=False,
    task_type=TaskType.CAUSAL_LM
)

model_config['model'] = get_peft_model(model_config['model'], lora_config)
model_config['model'].enable_input_require_grads()  
model_config['model'].gradient_checkpointing_enable() 

cclm = CustomCodeLlamaModel(model=model_config['model'], tokenizer=model_config['tokenizer'], sentence_model=sm, sentence_model_tokenizer=model_config['sentence_model_tokenizer'])
cclm.to(device)

optimizer_parameters = [p for p in model_config['model'].parameters()]

total_steps = int(len(train_dataloader) * args.num_train_epochs)
warmup_steps = int(total_steps * args.warmup_ratio)

"""
no_decay = ["LayerNorm.weight", "bias"]

# 正則化を適用しないパラメータ
optimizer_parameters.append({
    'params': [
        p for n, p in cclm.model.named_parameters()
        if any(nd in n for nd in no_decay)
    ],
    'weight_decay': 0.0,
    'lr': base_lr
})
"""

optimizer = AdamW(optimizer_parameters, lr=args.learning_rate, eps=args.adam_epsilon)
scheduler = get_linear_schedule_with_warmup(optimizer, num_warmup_steps=warmup_steps, num_training_steps=total_steps)

# Initialize lists to store loss values
train_loss_values = []
validation_loss_values = []

cclm.model.train()
num_steps = 0
for epoch in range(int(args.num_train_epochs)):
    train_loss = 0.0
    for batch in train_dataloader:
        codes = batch['code']
        labels = batch['labels'].to(device)
        outputs = cclm(original_codes=codes, labels=labels, model_config=model_config, args=args)
        
        loss, similarities, per_codes = outputs[0], outputs[1], outputs[2]
        similarities = similarities.detach().cpu().numpy()
        labels = labels.detach().cpu().numpy()
        for i in range(len(similarities)):
            print("------------------")
            print(f"epoch:{epoch}")
            print("tS------------------")
            print(codes[i])
            print("------------------")
            print(per_codes[i])
            print("------------------")
            print(similarities[i])
            print("------------------")
            print(labels[i])
            print("tE------------------")
        #loss.backward()
        optimizer.step()
        scheduler.step()
        cclm.zero_grad()

        #train_loss += loss.item()
        train_loss += loss
        num_steps += 1
    
    train_loss /= len(train_dataloader)
    train_loss_values.append(train_loss)
    print(f"Epoch: {epoch}, Training Loss: {train_loss}")

    cclm.model.eval()
    validation_loss = 0.0
    with torch.no_grad():
        for batch in validation_dataloader:
            codes = batch['code']
            labels = batch['labels'].to(device)
            outputs = cclm(original_codes=codes, labels=labels, model_config=model_config, args=args, eval=True)
            loss, similarities, per_codes = outputs[0], outputs[1], outputs[2]
            similarities = similarities.detach().cpu().numpy()
            labels = labels.detach().cpu().numpy()
            for i in range(len(similarities)):
                print("vS------------------")
                print(codes[i])
                print("------------------")
                print(per_codes[i])
                print("------------------")
                print(similarities[i])
                print("------------------")
                print(labels[i])
                print("vE------------------")
            validation_loss += loss

    validation_loss /= len(validation_dataloader)
    validation_loss_values.append(validation_loss)
    print(f"Validation Loss after epoch {epoch}: {validation_loss}")
    cclm.model.train()

#model_save(cclm)
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
cclm.model.save_pretrained("./saved_model/LoRA/model_"+timestamp)
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
        outputs = cclm(original_codes=codes, labels=labels, model_config=model_config, args=args, eval=True)
        loss, similarities, per_codes = outputs[0], outputs[1], outputs[2]
        
        similarities = similarities.detach().cpu().numpy()
        labels = labels.detach().cpu().numpy()
        for i in range(len(similarities)):
            print("S------------------")
            print(codes[i])
            print("------------------")
            print(per_codes[i])
            print("------------------")
            print(similarities[i])
            print("------------------")
            print(labels[i])
            print("E------------------")
        
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
