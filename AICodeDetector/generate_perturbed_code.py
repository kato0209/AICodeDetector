from masking import tokenize_and_mask
from preprocessing import preprocess_and_save
from load_model import load_mask_filling_model
from filling_mask import replace_masks
from extract_fill import extract_fills, apply_extracted_fills
from code_dataset import CodeDataset
import argparse
import torch
import os
import datetime
from torch.utils.data import DataLoader, random_split


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

# define the dataset
DATASET_PATH = 'datasets/Python/train'

human_codes = []
human_extensions = []
human_code_dir = os.path.join(DATASET_PATH, 'human')
for filename in os.listdir(human_code_dir):
    with open(os.path.join(human_code_dir, filename), 'r') as f:
        code = f.read()
        extension = os.path.splitext(filename)[1]  # ファイルから拡張子を抽出
        human_codes.append(code)
        human_extensions.append(extension)  # 拡張子をリストに保存

# chatGPTのコードを収集し、拡張子を保存
AI_codes = []
AI_extensions = []
AI_code_dir = os.path.join(DATASET_PATH, 'AI')
for filename in os.listdir(AI_code_dir):
    with open(os.path.join(AI_code_dir, filename), 'r') as f:
        code = f.read()
        extension = os.path.splitext(filename)[1]
        AI_codes.append(code)
        AI_extensions.append(extension)


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

batch_size = 16
file_path = 'datasets_mask_fill/Python/yake'

# 各バッチでの処理、拡張子も動的に適用
for i in range(0, len(human_codes), batch_size):
    batch_codes = human_codes[i:i + batch_size]
    batch_extensions = human_extensions[i:i + batch_size]  # 対応する拡張子のバッチ
    human_masked_codes, human_perturbed_codes = pertubate_code(batch_codes, model_config, args)

    for c, (original_code, ext) in enumerate(zip(batch_codes, batch_extensions)):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"{file_path}/human/original-{c}-{timestamp}{ext}"
        with open(output_file, 'w') as file:
            file.write(original_code)

    for j, (code, ext) in enumerate(zip(human_masked_codes, batch_extensions)):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"{file_path}/human/mask-{j}-{timestamp}{ext}"
        with open(output_file, 'w') as file:
            file.write(code)

    for k, (code, ext) in enumerate(zip(human_perturbed_codes, batch_extensions)):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"{file_path}/human/fill-{k}-{timestamp}{ext}"
        with open(output_file, 'w') as file:
            file.write(code)

# AIコードの処理も同様に行う
for i in range(0, len(AI_codes), batch_size):
    batch_codes = AI_codes[i:i + batch_size]
    batch_extensions = AI_extensions[i:i + batch_size]
    AI_masked_codes, AI_perturbed_codes = pertubate_code(batch_codes, model_config, args)

    for c, (original_code, ext) in enumerate(zip(batch_codes, batch_extensions)):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"{file_path}/AI/original-{c}-{timestamp}{ext}"
        with open(output_file, 'w') as file:
            file.write(original_code)

    for j, (code, ext) in enumerate(zip(AI_masked_codes, batch_extensions)):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"{file_path}/AI/mask-{j}-{timestamp}{ext}"
        with open(output_file, 'w') as file:
            file.write(code)

    for k, (code, ext) in enumerate(zip(AI_perturbed_codes, batch_extensions)):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"{file_path}/AI/fill-{k}-{timestamp}{ext}"
        with open(output_file, 'w') as file:
            file.write(code)
