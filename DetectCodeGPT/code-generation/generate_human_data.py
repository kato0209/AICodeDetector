import time
import openai
import numpy as np
import re
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForSeq2SeqLM
from loguru import logger
import gzip
import json
import pdb
from tqdm import tqdm
import os
import argparse

# os.environ["CUDA_VISIBLE_DEVICES"] = "0"
os.environ["TOKENIZERS_PARALLELISM"] = "false"

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# device = torch.device('cpu')


def load_data(directory_path='data/CodeSearchNet', path_to_data=None, language='python', max_num=10000):

    all_prompts = []
    all_solutions = []

    if 'humaneval' in directory_path:
        path_to_data = f'{directory_path}/{language}/data/humaneval_{language}.jsonl.gz'

        logger.info(f'Loading data from {path_to_data}')

        with gzip.open(path_to_data, 'rb') as f:

            for line in f:
                data = json.loads(line)

                all_prompts.append(data['prompt'])
                all_solutions.append(data['canonical_solution'])

    elif 'CodeSearchNet' in directory_path:

        
        #path_to_data = f'{path}/{language}/final/jsonl/test/python_test_0.jsonl.gz'
        #path_to_data = f'{directory_path}/{language}/final/jsonl/test/python_test_0.jsonl'

        logger.info(f'Loading data from {path_to_data}')

        failed = 0
        success = 0

        max_prompt_len = 128
        min_prompt_len = 5

        max_solution_len = 256
        min_solution_len = 5

        with gzip.open(path_to_data, 'rt', encoding='utf-8') as f:

            count = 0
            for line in tqdm(f):

                data = json.loads(line)

                data['original_string'] = data['original_string'].replace("'''", '"""')
                try:
                    prompt = data['original_string'].split('"""')[0] + '"""' + data['original_string'].split('"""')[1] + '"""'
                    solution = data['original_string'].split('"""')[2]
                    success += 1
                except:
                    failed += 1


                if len(prompt.split()) > max_prompt_len or len(prompt.split()) < min_prompt_len:
                    continue

                if len(solution.split()) > max_solution_len or len(solution.split()) < min_solution_len:
                    continue

                all_prompts.append(prompt)
                all_solutions.append(solution)

        logger.info(f'Failed: {failed}, Success: {success}')

    elif "TheVault" in directory_path:

        path_to_data = f'{directory_path}/small_train.jsonl'

        logger.info(f'Loading data from {path_to_data}')

        failed = 0
        success = 0

        max_prompt_len = 128
        min_prompt_len = 5

        max_solution_len = 256
        min_solution_len = 5

        with open(path_to_data, 'r') as f:

            count = 0
            for line in tqdm(f):

                data = json.loads(line)

                data['original_string'] = data['original_string'].replace("'''", '"""')
                try:
                    prompt = data['original_string'].split('"""')[0] + '"""' + data['original_string'].split('"""')[1] + '"""'
                    solution = data['original_string'].split('"""')[2]
                    success += 1
                except:
                    failed += 1


                if len(prompt.split()) > max_prompt_len or len(prompt.split()) < min_prompt_len:
                    continue

                if len(solution.split()) > max_solution_len or len(solution.split()) < min_solution_len:
                    continue

                all_prompts.append(prompt)
                all_solutions.append(solution)

        logger.info(f'Failed: {failed}, Success: {success}')

    logger.info(f'Loaded {len(all_prompts)} prompts and {len(all_solutions)} solutions')

    # analyze the lengths
    prompt_lengths = [len(prompt.split()) for prompt in all_prompts]
    solution_lengths = [len(solution.split()) for solution in all_solutions]
    logger.info(f'Prompt lengths: min: {min(prompt_lengths)}, max: {max(prompt_lengths)}, mean: {np.mean(prompt_lengths)}, std: {np.std(prompt_lengths)}')
    logger.info(f'Solution lengths: min: {min(solution_lengths)}, max: {max(solution_lengths)}, mean: {np.mean(solution_lengths)}, std: {np.std(solution_lengths)}')

    if len(all_prompts) > max_num:

        seed = 42
        np.random.seed(seed)
        indices = np.random.choice(len(all_prompts), max_num, replace=False)
        all_prompts = [all_prompts[i] for i in indices]
        all_solutions = [all_solutions[i] for i in indices]

        prompt_lengths = [len(prompt.split()) for prompt in all_prompts]
        solution_lengths = [len(solution.split()) for solution in all_solutions]

        logger.info(f'Sampled {len(all_prompts)} prompts and {len(all_solutions)} solutions')
        logger.info(f'Prompt lengths: min: {min(prompt_lengths)}, max: {max(prompt_lengths)}, mean: {np.mean(prompt_lengths)}, std: {np.std(prompt_lengths)}')
        logger.info(f'Solution lengths: min: {min(solution_lengths)}, max: {max(solution_lengths)}, mean: {np.mean(solution_lengths)}, std: {np.std(solution_lengths)}')

    return all_prompts, all_solutions


def truncate(completion):

    def find_re(string, pattern, start_pos):
        m = pattern.search(string, start_pos)
        return m.start() if m else -1

    terminals = [
        re.compile(r, re.MULTILINE)
        for r in
        [
            re.escape('<|endoftext|>')
        ]
    ]


    start_pos = 0

    terminals_pos = [pos for pos in [find_re(completion, terminal, start_pos) for terminal in terminals] if pos != -1]
    if len(terminals_pos) > 0:
        return completion[:min(terminals_pos)]
    else:
        return completion

if __name__ == "__main__":

    # path = 'data/CodeSearchNet'
    # path = "data/TheVault"

    parser = argparse.ArgumentParser()
    #parser.add_argument('--path', type=str, default="data/TheVault")
    parser.add_argument('--path', type=str, default="data/CodeSearchNet")
    parser.add_argument('--max_num', type=int, default=10000)
    parser.add_argument('--temperature', type=float, default=0.2)
    #parser.add_argument('--model_name', type=str, default='codellama/CodeLlama-7b-hf')
    #parser.add_argument('--model_name', type=str, default='facebook/incoder-1B')
    #parser.add_argument('--model_name', type=str, default='AlekseyKorshuk/WizardCoder-3B-V1.0-dpo-beta-0.01')
    #parser.add_argument('--model_name', type=str, default='Salesforce/codegen2-3_7B_P')
    #parser.add_argument('--model_name', type=str, default='bigcode/starcoderbase-3b')
    #parser.add_argument('--model_name', type=str, default='microsoft/phi-1')
    parser.add_argument('--batch_size', type=int, default=16)
    parser.add_argument('--max_length', type=int, default=128)
    args = parser.parse_args()

    logger.info(f'args: {args}')

    path = args.path
    max_num = args.max_num
    #model_name = args.model_name
    batch_size = args.batch_size

    data_paths = [
        "data/CodeSearchNet/python/final/jsonl/train/python_train_1.jsonl.gz",
        "data/CodeSearchNet/python/final/jsonl/train/python_train_2.jsonl.gz",
        "data/CodeSearchNet/python/final/jsonl/train/python_train_3.jsonl.gz",
        "data/CodeSearchNet/python/final/jsonl/train/python_train_4.jsonl.gz",
        "data/CodeSearchNet/python/final/jsonl/train/python_train_5.jsonl.gz",
    ]

    # max_num = 100000
    for path in data_paths:
    
        prompts, solutions = load_data(directory_path=path, path_to_data=path, language='python', max_num=max_num)

        # write the outputs to a file and together with the prompts and solutions

        save_prefix = f'output/{path.split("/")[-1]}'

        if args.max_length >= 256:
            file_name = f'{save_prefix}/human-{max_num}-nostop-{path}/outputs.txt'
            if not os.path.exists(f'{save_prefix}/human-{max_num}-nostop-{path}'):
                os.makedirs(f'{save_prefix}/human-{max_num}-nostop-{path}')
        else:
            file_name = f'{save_prefix}/human-{max_num}-{path}/outputs.txt'
            if not os.path.exists(f'{save_prefix}/human-{max_num}-{path}'):
                os.makedirs(f'{save_prefix}/human-{max_num}-{path}')
        if os.path.exists(file_name):
            os.remove(file_name)

        with open(file_name, 'w+') as f:
            for i in range(len(solutions)):
                results = {'prompt': prompts[i], 'solution': solutions[i]}
                f.write(json.dumps(results))
                f.write('\n')

        # another version that is more clear with printing
        file_name = f'{save_prefix}/human-{max_num}-{path}/outputs_v2.txt'

        # delete the file if it exists
        if os.path.exists(file_name):
            os.remove(file_name)

        logger.info(f'Finished writing to {file_name}')
