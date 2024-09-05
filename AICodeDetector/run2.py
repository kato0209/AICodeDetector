from loguru import logger
from tqdm import tqdm

from masking import tokenize_and_mask
from preprocessing import preprocess_and_save
from load_model import load_mask_filling_model, load_model
from filling_mask import replace_masks
from extract_fill import extract_fills, apply_extracted_fills
from code_dataset import CodeDataset, CodeDatasetFromCodeSearchNet, CodeDatasetRewriting, CodeDatasetSimilarity
import argparse
import torch
import os
import datetime
from torch.utils.data import DataLoader, random_split

from model import CustomBertModel
from transformers.optimization import AdamW, get_linear_schedule_with_warmup
from utils.model_save import model_save
from utils.confusion_matrix import plot_confusion_matrix
from pertube_data import pertube_data

from sklearn.metrics import accuracy_score, roc_auc_score
from datetime import datetime
import random
import logging
from sklearn.metrics import classification_report, confusion_matrix
from utils.generate_cs_data import generate_data

import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
from utils.download_data import download_data_from_json

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
parser.add_argument("--learning_rate", default=1e-5, type=float)
parser.add_argument("--adam_epsilon", default=1e-6, type=float)
parser.add_argument("--num_train_epochs", default=30, type=float)
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
#model_config = load_model(args, args.base_model_name, model_config)

#ai_data = download_data_from_json('rewrite_dataset/_rewrite_code_by_gpt_AI_rewrite_Revise the code with your best effort.json')
#human_data = download_data_from_json('rewrite_dataset/_rewrite_code_by_gpt_Human_rewrite_Revise the code with your best effort.json')

#ai_data = download_data_from_json('json_data/rewrite_code_GPT_inv.json')
#human_data = download_data_from_json('json_data/rewrite_code_human_inv.json')

dataset_paths =[
    'rewrite_dataset/Train_Rewrite_code_by_gpt_AI_HumanEval_codellama.json',
    #'rewrite_dataset/Train_Rewrite_code_by_gpt_AI_HumanEval_incoder.json'
]

ai_data = {
    "original": [],
    "rewrite": []
}

for path in dataset_paths:
    sep_data = download_data_from_json(path)
    ai_data["original"] = ai_data["original"] + sep_data["original"]
    ai_data["rewrite"] = ai_data["rewrite"] + sep_data["rewrite"]

#ai_data = download_data_from_json('rewrite_dataset/Rewrite_code_by_gpt_AI_HumanEval_codellama.json')
human_data = download_data_from_json('rewrite_dataset/Train_Rewrite_code_by_gpt3-5_Human.json')

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


from sentence_transformers import InputExample
train_dataset = []
for i in range(len(train_data["human"]["original"])):
    train_dataset.append(InputExample(texts=[train_data["human"]["original"][i], train_data["human"]["rewrite"][i]], label=0))

for i in range(len(train_data["ai"]["original"])):
    train_dataset.append(InputExample(texts=[train_data["ai"]["original"][i], train_data["ai"]["rewrite"][i]], label=1))

val_dataset = []
for i in range(len(val_data["human"]["original"])):
    val_dataset.append(InputExample(texts=[val_data["human"]["original"][i], val_data["human"]["rewrite"][i]], label=0))

for i in range(len(val_data["ai"]["original"])):
    val_dataset.append(InputExample(texts=[val_data["ai"]["original"][i], val_data["ai"]["rewrite"][i]], label=1))

test_dataset = []
for i in range(len(test_data["human"]["original"])):
    test_dataset.append(InputExample(texts=[test_data["human"]["original"][i], test_data["human"]["rewrite"][i]], label=0))

for i in range(len(test_data["ai"]["original"])):
    test_dataset.append(InputExample(texts=[test_data["ai"]["original"][i], test_data["ai"]["rewrite"][i]], label=1))


train_dataloader = DataLoader(train_dataset, shuffle=True, batch_size=32)

total_steps = int(len(train_dataloader) * args.num_train_epochs)
warmup_steps = int(total_steps * args.warmup_ratio)

from sentence_transformers.cross_encoder import CrossEncoder
from sentence_transformers.cross_encoder.evaluation import CEF1Evaluator, CESoftmaxAccuracyEvaluator
from sentence_transformers.evaluation import SequentialEvaluator
from sentence_transformers.cross_encoder.evaluation import CECorrelationEvaluator
model = CrossEncoder("microsoft/codebert-base", num_labels=1)

evaluator = CECorrelationEvaluator.from_input_examples(test_dataset, name="sts-dev")


model_save_path = "saved_model/crossModel_" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
model.fit(
    train_dataloader=train_dataloader,
    evaluator=evaluator,
    epochs=args.num_train_epochs,
    evaluation_steps=100,
    warmup_steps=warmup_steps,
    output_path=model_save_path,
)