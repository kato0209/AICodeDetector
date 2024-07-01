from loguru import logger
from tqdm import tqdm

from masking import tokenize_and_mask
from preprocessing import preprocess_and_save
from load_model import load_mask_filling_model, load_model2
from filling_mask import replace_masks
from extract_fill import extract_fills, apply_extracted_fills
from code_dataset import CodeDatasetCS, CodeDatasetFromCodeSearchNet
import argparse
import torch
import os
import datetime
from torch.utils.data import DataLoader, random_split

from model import CustomBertModel, SimilarityModel
from pertubate import rewrite_code
from transformers.optimization import AdamW, get_linear_schedule_with_warmup
from utils.model_save import model_save, similarity_model_save
from utils.confusion_matrix import plot_confusion_matrix
from utils.generate_cs_data import generate_data_human
from pertube_data import pertube_data

from sklearn.metrics import accuracy_score, roc_auc_score
from datetime import datetime
import random
import logging
from sklearn.metrics import classification_report, confusion_matrix

import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

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
parser.add_argument("--learning_rate", default=2e-6, type=float)
parser.add_argument("--adam_epsilon", default=1e-6, type=float)
parser.add_argument("--num_train_epochs", default=20, type=float)
parser.add_argument("--warmup_ratio", default=0.01, type=float)
parser.add_argument("--weight_decay", default=0.05, type=float)

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
    'base_model_name': "codellama/CodeLlama-7b-hf",
    'mask_filling_model_name': "Salesforce/codet5p-770m",
    'batch_size': 64,
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
model_config = {}
model_config = load_model2(args, args.base_model_name, model_config)
#model_config = load_model(args, args.base_model_name, model_config)

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
#                line['solution'] = line['solution'].split('def')[0]
#
#            # I don't like there to have too many 'def' in the code
#            # ~100/100000 examples have more than 3 'def'
#            if line['solution'].count('def') > max_def_num:
#                max_def_num_count += 1
#                continue
#
#            # avoid examples that are too short (less than min_len words)
#            # around 2000/100000 examples have around 55 words
#            if len(line['solution'].split()) < min_len:
#                min_len_count += 1
#                continue
#
#            # if the are too many comments, skip
#            def count_comment(text):
#                return text.count('#')
#
#            if count_comment(line['solution']) > max_comment_num:
#                max_comment_num_count += 1
#                continue
#
#            # if there are too many TODOs, skip
#            def count_todo_comment(text):
#                return text.count('# TODO') + text.count('# todo')
#
#            if count_todo_comment(line['solution']) > max_todo_num:
#                max_todo_num_count += 1
#                continue
#
#            # the number of text.count("'''") and text.count('"""') should be <1
#            if line['solution'].count("'''") > 0 or line['solution'].count('"""') > 0:
#                function_comment_num_count += 1
#                continue
#
#            # cut to 128 tokens
#            all_originals.append(' '.join(line['solution'].split(' ')[:max_len]))
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
#
#    data = {
#        "original": all_originals,
#        "sampled": all_samples
#    }
#
#    return data

datasets_paths = [
    "CSHumanDatasets/outputs_train1.txt",
    "CSHumanDatasets/outputs_train2.txt",
    "CSHumanDatasets/outputs_train3.txt",
    "CSHumanDatasets/outputs_train4.txt",
    "CSHumanDatasets/outputs_train5.txt",
    "CSHumanDatasets/outputs_train6.txt",
    "CSHumanDatasets/outputs_train7.txt",
    "CSHumanDatasets/outputs_train8.txt",
    "CSHumanDatasets/outputs_train9.txt",
    "CSHumanDatasets/outputs_train10.txt",
    "CSHumanDatasets/outputs_train11.txt",
    "CSHumanDatasets/outputs_train12.txt",
    "CSHumanDatasets/outputs_train13.txt",
]

data = {
    "original": []
}
i = 0
for path in datasets_paths:
    sep_data = generate_data_human(path=path)
    data["original"] = data["original"] + sep_data["original"]
    i += 1

data["original"] = list(set(data["original"]))

train_data = {
    "original": data["original"][:int(len(data["original"])*0.7)]
}

val_data = {
    "original": data["original"][int(len(data["original"])*0.7):int(len(data["original"])*0.8)]
}

test_data = {
    "original": data["original"][int(len(data["original"])*0.8):]
}

"""
# train_dataを先頭の10件に
train_data["original"] = train_data["original"][:1]
train_data["sampled"] = train_data["sampled"][:1]

# val_dataを先頭の10件に
val_data["original"] = val_data["original"][:1]
val_data["sampled"] = val_data["sampled"][:1]

# test_dataを先頭の10件に
test_data["original"] = test_data["original"][:1]
test_data["sampled"] = test_data["sampled"][:1]
"""

train_dataset = CodeDatasetCS(train_data, model_config, args)
val_dataset = CodeDatasetCS(val_data, model_config, args)
test_dataset = CodeDatasetCS(test_data, model_config, args)

train_dataloader = DataLoader(train_dataset, args.batch_size, shuffle=True)
validation_dataloader = DataLoader(val_dataset, args.batch_size, shuffle=False)
test_dataloader = DataLoader(test_dataset, args.batch_size, shuffle=False)

sm = SimilarityModel(model=model_config["model"], tokenizer=model_config["tokenizer"])
sm.to(device)

total_steps = int(len(train_dataloader) * args.num_train_epochs)
warmup_steps = int(total_steps * args.warmup_ratio)

base_lr = args.learning_rate

optimizer_parameters = []
no_decay = ["LayerNorm.weight", "bias"]

# 正則化を適用しないパラメータ
optimizer_parameters.append({
    'params': [
        p for n, p in sm.model.named_parameters()
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

sm.train()
num_steps = 0
for epoch in range(int(args.num_train_epochs)):
    train_loss = 0.0
    cosine_loss = 0.0
    for batch in train_dataloader:
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)

        outputs = sm(input_ids, attention_mask=attention_mask)
        loss, logits = outputs[0], outputs[1]
        loss.backward()
        optimizer.step()
        scheduler.step()
        sm.zero_grad()

        train_loss += loss.item()
        num_steps += 1

    train_loss /= len(train_dataloader)
    train_loss_values.append(train_loss)
    print(f"Epoch: {epoch}, Training Loss: {train_loss}, Cosine Loss: {cosine_loss}")

    sm.eval()
    validation_loss = 0.0
    with torch.no_grad():
        for batch in validation_dataloader:
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            outputs = sm(input_ids, attention_mask=attention_mask)
            loss = outputs[0]
            validation_loss += loss.item()

    validation_loss /= len(validation_dataloader)
    validation_loss_values.append(validation_loss)
    print(f"Validation Loss after epoch {epoch}: {validation_loss}")
    sm.train()

similarity_model_save(sm)
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
plt.savefig(f"./learning_result/learning_curve_sm{timestamp}.png")
