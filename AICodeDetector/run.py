from loguru import logger
from tqdm import tqdm

from masking import tokenize_and_mask
from preprocessing import preprocess_and_save
from load_model import load_mask_filling_model
from filling_mask import replace_masks
from extract_fill import extract_fills, apply_extracted_fills
from code_dataset import CodeDataset, CodeDatasetFromCodeSearchNet
import argparse
import torch
import os
import datetime
from torch.utils.data import DataLoader, random_split

from model import CustomBertModel
from transformers.optimization import AdamW, get_linear_schedule_with_warmup
from utils.model_save import model_save
from utils.confusion_matrix import plot_confusion_matrix

from sklearn.metrics import accuracy_score
from datetime import datetime
import logging
from sklearn.metrics import classification_report, confusion_matrix

import numpy as np
import scipy.stats

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
parser.add_argument('--batch_size', type=int, default=5)
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
parser.add_argument("--num_train_epochs", default=12, type=float)
parser.add_argument("--warmup_ratio", default=0.06, type=float)
parser.add_argument("--weight_decay", default=0.01, type=float)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

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
    'batch_size': 50,
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
    'DEVICE': device,
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

model_config = {}
model_config = load_mask_filling_model(args, args.mask_filling_model_name, model_config)

def generate_data(max_num=500, min_len=0, max_len=128, max_comment_num=10, max_def_num=5, cut_def=False, max_todo_num=3, path=None):

    logger.info(f'Loading data from {path}')
    import json
    all_originals = []
    all_samples = []  # machine generated

    max_def_num_count = 0
    min_len_count = 0
    max_comment_num_count = 0
    function_comment_num_count = 0
    max_todo_num_count = 0

    with open(path, 'r') as f:
        for line in tqdm(f, ncols=70):
            line = line.strip()
            if line == '':
                continue
            line = json.loads(line)

            # cut out the 'def' part after the first generation
            if cut_def:
                line['output'] = line['output'].split('def')[0]
                line['solution'] = line['solution'].split('def')[0]

            # I don't like there to have too many 'def' in the code
            # ~100/100000 examples have more than 3 'def'
            if line['solution'].count('def') > max_def_num or line['output'].count('def') > max_def_num:
                max_def_num_count += 1
                continue

            # avoid examples that are too short (less than min_len words)
            # around 2000/100000 examples have around 55 words
            if len(line['solution'].split()) < min_len or len(line['output'].split()) < min_len:
                min_len_count += 1
                continue

            # if the are too many comments, skip
            def count_comment(text):
                return text.count('#')

            if count_comment(line['solution']) > max_comment_num or count_comment(line['output']) > max_comment_num:
                max_comment_num_count += 1
                continue

            # if there are too many TODOs, skip
            def count_todo_comment(text):
                return text.count('# TODO') + text.count('# todo')

            if count_todo_comment(line['solution']) > max_todo_num or count_todo_comment(line['output']) > max_todo_num:
                max_todo_num_count += 1
                continue

            # the number of text.count("'''") and text.count('"""') should be <1
            if line['solution'].count("'''") > 0 or line['solution'].count('"""') > 0 or line['output'].count("'''") > 0 or line['output'].count('"""') > 0:
                function_comment_num_count += 1
                continue

            # cut to 128 tokens
            all_originals.append(' '.join(line['solution'].split(' ')[:max_len]))
            all_samples.append(' '.join(line['output'].split(' ')[:max_len]))

    logger.info(f'{max_def_num_count} examples have more than {max_def_num} "def"')
    logger.info(f'{min_len_count} examples have less than {min_len} words')
    logger.info(f'{max_comment_num_count} examples have more than {max_comment_num} comments')
    logger.info(f'{max_todo_num_count} examples have more than {max_todo_num} TODOs')
    logger.info(f'{function_comment_num_count} examples have more than 1 function comment')
    logger.info(f'Loaded {len(all_originals)} examples after filtering, and will return {min(max_num, len(all_originals))} examples')

    # statistical analysis
    # import random
    # random.seed(42)
    # random.shuffle(all_originals)
    # random.shuffle(all_samples)

    data = {
        "original": all_originals[:max_num],
        "sampled": all_samples[:max_num]
    }

    return data

def random_insert_space(text, pct=0.3, mean=1):
    '''
    randomly insert a space for pct of the lines
    '''
    tokens = text.split(' ')
    n_tokens = len(tokens)
    n_inserted = int(n_tokens * pct)
    inserted_idxs = np.random.choice(n_tokens, n_inserted, replace=False)
    for idx in inserted_idxs:
        n_spaces = scipy.stats.poisson.rvs(mean) + 1
        # n_spaces = 1
        tokens[idx] = tokens[idx] + ' '*n_spaces
    return ' '.join(tokens)

def random_insert_newline(text, pct=0.3, mean=1):
    '''
    randomly insert a newline for pct of the lines
    '''
    lines = text.split('\n')
    n_lines = len(lines)
    n_inserted = int(n_lines * pct)
    inserted_idxs = np.random.choice(n_lines, n_inserted, replace=False)
    for idx in inserted_idxs:
        n_newlines = 1
        # n_newlines = scipy.stats.poisson.rvs(mean) + 1
        lines[idx] = lines[idx] + '\n'*n_newlines
    return '\n'.join(lines)

def random_insert_newline_space(texts, pct=0.5, lambda_poisson=2):
    perturbed_texts_part1 = [random_insert_space(x, pct, lambda_poisson) for x in texts]
    perturbed_texts_part2 = [random_insert_newline(x, pct, lambda_poisson) for x in texts]
    total_num = len(perturbed_texts_part1)
    n1 = int(total_num / 2)
    n2 = total_num - n1
    perturbed_texts_part1 = perturbed_texts_part1[:n1]
    perturbed_texts_part2 = perturbed_texts_part2[:n2]
    return perturbed_texts_part1 + perturbed_texts_part2

def pertubate_code(codes, model_config, args):
    span_length = 2
    pct = 0.3
    buffer_size = 1
    #masked_text = tokenize_and_mask(tokens, buffer_size, span_length, pct, ceil_pct=False)
    masked_codes = [tokenize_and_mask(x, buffer_size, span_length, pct, ceil_pct=False) for x in codes]

    raw_fills = replace_masks(masked_codes, model_config, args)
    #print(raw_fills)
    extracted_fills = extract_fills(raw_fills)
    #print(extracted_fills)
    perturbed_codes = apply_extracted_fills(masked_codes, extracted_fills)
    #print(perturbed_texts)

    return masked_codes, perturbed_codes 

datasets_paths = [
    "CodeSearchNetDatasets/outputs_incoder_0.2.txt",
    "CodeSearchNetDatasets/outputs_phi1_0.2.txt",
    "CodeSearchNetDatasets/outputs_starcoder_0.2.txt",
    "CodeSearchNetDatasets/outputs_wizardcoder_0.2.txt",
    "CodeSearchNetDatasets/outputs_codegen2_0.2.txt",
    "CodeSearchNetDatasets/outputs_Llama_0.2.txt",
]

data = {
    "original": [],
    "sampled": []
}
i = 0
for path in datasets_paths:
    sep_data = generate_data(path=path)
    if i == 0:
        data["original"] = data["original"] + sep_data["original"]
    data["sampled"] = data["sampled"] + sep_data["sampled"]
    i += 1


perturbation_type = 'space-line'
if perturbation_type == 'space-line':
    human_codes_perturbed = random_insert_newline_space(data["original"])
    AI_codes_perturbed = random_insert_newline_space(data["sampled"])
    data["original"] = data["original"] + human_codes_perturbed
    data["sampled"] = data["sampled"] + AI_codes_perturbed
else:
    batch_size = 16
    all_human_codes = data["original"]
    all_human_masked_codes = []
    all_human_perturbed_codes = []

    all_AI_codes = data["sampled"]
    all_AI_masked_codes = []
    all_AI_perturbed_codes = []

    # 各バッチでの処理、拡張子も動的に適用
    for i in range(0, len(all_human_codes), batch_size):
        batch_codes = all_human_codes[i:i + batch_size]
        human_masked_codes, human_perturbed_codes = pertubate_code(batch_codes, model_config, args)
        all_human_masked_codes += human_masked_codes
        all_human_perturbed_codes += human_perturbed_codes
        

    # AIコードの処理も同様に行う
    for i in range(0, len(all_AI_codes), batch_size):
        batch_codes = all_AI_codes[i:i + batch_size]
        AI_masked_codes, AI_perturbed_codes = pertubate_code(batch_codes, model_config, args)
        all_AI_masked_codes += AI_masked_codes
        all_AI_perturbed_codes += AI_perturbed_codes

    data["original"] = all_human_codes + all_human_masked_codes + all_human_perturbed_codes
    data["sampled"] = all_AI_codes + all_AI_masked_codes + all_AI_perturbed_codes



datasets = CodeDatasetFromCodeSearchNet(data, model_config, args)
# データセットの全長を取得
dataset_size = len(datasets)
train_size = int(0.8 * dataset_size)
test_size = dataset_size - train_size

# データセットをランダムに分割
train_dataset, test_dataset = random_split(datasets, [train_size, test_size])

train_dataloader = DataLoader(train_dataset, batch_size=32, shuffle=True)
test_dataloader = DataLoader(test_dataset, batch_size=32, shuffle=False)

cbm = CustomBertModel()
cbm.to(device)

total_steps = int(len(train_dataloader) * args.num_train_epochs)
warmup_steps = int(total_steps * args.warmup_ratio)
no_decay = ["LayerNorm.weight", "bias"]
optimizer_grouped_parameters = [
    {
        "params": [p for n, p in cbm.named_parameters() if not any(nd in n for nd in no_decay)],
        "weight_decay": args.weight_decay,
    },
    {"params": [p for n, p in cbm.named_parameters() if any(nd in n for nd in no_decay)], "weight_decay": 0.0},
]
optimizer = AdamW(optimizer_grouped_parameters, lr=args.learning_rate, eps=args.adam_epsilon)
scheduler = get_linear_schedule_with_warmup(optimizer, num_warmup_steps=warmup_steps, num_training_steps=total_steps)

cbm.train()
num_steps = 0
for epoch in range(int(args.num_train_epochs)):
    for batch in train_dataloader:
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        labels = batch['labels'].to(device)
        outputs = cbm(input_ids, attention_mask=attention_mask, labels=labels)
        loss, cos_loss = outputs[0], outputs[1]
        loss.backward()
        optimizer.step()
        scheduler.step()
        cbm.zero_grad()
        num_steps += 1
        print(f"Epoch: {epoch}, Step: {num_steps}, Loss: {loss.item()}, Cosine Loss: {cos_loss.item()}")

model_save(cbm)
print("done training")


# Test the model and print out the confusion matrix
log_path = './logs'
os.makedirs(log_path, exist_ok=True)
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
logging.basicConfig(filename=os.path.join(log_path, f'test_{timestamp}.log'),
                    force=True,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)

cbm.eval()
label_list, pred_list = [], []
with torch.no_grad():
    for batch in test_dataloader:
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        outputs = cbm(input_ids, attention_mask=attention_mask)
        labels = batch["labels"]
        logits = outputs[0]
        predictions = torch.argmax(logits, dim=1)
        label_list += labels.tolist()
        pred_list += predictions.tolist()

accuracy = accuracy_score(label_list, pred_list)
print(label_list)
print(pred_list)
print(accuracy)


target_names = ['ChatGPT','Human']
logging.info('Confusion Matrix')
cm = confusion_matrix(label_list, pred_list)
plot_confusion_matrix(cm, target_names, title='Confusion Matrix')
logging.info('Classification Report')
logging.info(classification_report(label_list, pred_list, target_names=target_names))
