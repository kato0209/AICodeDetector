import os
import openai
import json
import time
import openai
import numpy as np
import re
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForSeq2SeqLM
from loguru import logger
import gzip
import pdb
from tqdm import tqdm
import argparse

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

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
def generate_hf(model_name, prompts, solutions, batch_size=16, max_length_sample=128, max_length=128, do_sample=True, top_p=0.95, temperature=0.2):
    # prompts に文字列を追加して再生成する
    new_prompts = []
    for i in range(len(prompts)):
        prompt = f"Help me write python code start with this {prompts[i]}, no explanation, just code:"
        new_prompts.append(prompt)
    prompts = new_prompts
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    if 'codegen-' in model_name.lower():
        tokenizer.pad_token_id = 50256
        tokenizer.padding_side = 'left'
    elif 'santa' in model_name.lower():
        tokenizer.pad_token_id = 49156  # https://huggingface.co/bigcode/santacoder/blob/main/special_tokens_map.json
        logger.info(f'pad_token: {tokenizer.pad_token}')
        tokenizer.padding_side = 'left'
    elif 'parrot' in model_name.lower():
        tokenizer.pad_token_id = tokenizer.eos_token_id
        logger.info(f'pad_token: {tokenizer.pad_token}')
        tokenizer.padding_side = 'left'
    elif "incoder" in model_name.lower():
        tokenizer.pad_token_id = 1
        tokenizer.padding_side = 'left'
    elif "phi-1" in model_name.lower():
        tokenizer.pad_token_id = tokenizer.eos_token_id
        logger.info(f'pad_token: {tokenizer.pad_token}')
        tokenizer.padding_side = 'left'

    if 't5p' in model_name.lower():
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name,
                                                      torch_dtype=torch.float16,
                                                      trust_remote_code=True)
    # todo: not sure wizard for tp16
    elif "llama" in model_name.lower() or "wizard" in model_name.lower():
        model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True, torch_dtype=torch.float16)
    elif "codegen2" in model_name.lower():
        model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True, revision="main")
    else:
        model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True)

    all_outputs = []
    model = model.to(device)

    if 'starcoder' in model_name.lower() or "llama" in model_name.lower() or "wizard" in model_name.lower() or "codegen2" in model_name.lower():
        input_ids = [tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512).input_ids for prompt in prompts]

        def_id = tokenizer('def', add_special_tokens=False).input_ids[0]
        try:
            def_with_space_id = tokenizer('def', add_prefix_space=True, add_special_tokens=False).input_ids[0]
        except:
            def_with_space_id = tokenizer(' def', add_special_tokens=False).input_ids[0]

        eos_id_list = [tokenizer.eos_token_id, def_id, def_with_space_id]
        logger.info(f'eos_id_list: {eos_id_list}')

        for input_ids in tqdm(input_ids, ncols=50):
            input_ids = input_ids.to(device)
            input_ids_len = input_ids.shape[1]
            logger.info(f'input_ids_len: {input_ids_len}')

            if max_length_sample >= 256:
                outputs = model.generate(input_ids, do_sample=do_sample, max_length=max_length_sample+input_ids_len, top_p=top_p, temperature=temperature, pad_token_id=tokenizer.pad_token_id, use_cache=True, eos_token_id=eos_id_list)
            else:
                outputs = model.generate(input_ids, do_sample=do_sample, max_length=max_length_sample+input_ids_len, top_p=top_p, temperature=temperature, pad_token_id=tokenizer.pad_token_id, use_cache=True)

            decoded_output = tokenizer.decode(outputs[0, input_ids_len:])
            # logger.info(f'decoded_output: {decoded_output}')
            all_outputs.append(decoded_output)
            outputs = all_outputs
    else:
        input_ids = tokenizer(prompts, return_tensors="pt", padding=True, truncation=True, max_length=512).input_ids
        input_ids_len = input_ids.shape[1]
        logger.info(f'input_ids_len: {input_ids_len}')

        # create a dataset from the samples
        dataset = torch.utils.data.TensorDataset(input_ids)

        if batch_size >= 4:
            num_workers = batch_size // 2
        else:
            num_workers = 1

        dataloader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, pin_memory=True, num_workers=num_workers)

        for input_ids in tqdm(dataloader, ncols=50):

            input_ids = input_ids[0].to(device)
            outputs = model.generate(input_ids, do_sample=do_sample, max_length=max_length_sample+input_ids_len, top_p=top_p, temperature=temperature, pad_token_id=tokenizer.pad_token_id, use_cache=True)
            
            all_outputs.append(outputs)

        samples = torch.cat(all_outputs, dim=0)
        outputs = tokenizer.batch_decode(samples[:, input_ids_len:, ...])

    # truncate the outputs (based on the original code of CodeGen)
    outputs = [truncate(output) for output in outputs]
    from util_func import remove_blank_lines
    outputs = [remove_blank_lines(output) for output in outputs]

    logger.info(f'Generated {len(outputs)} samples')

    logger.info("Showing first 3 samples")

    for i in range(3):
        logger.info(f'Example {i}:')
        logger.info(f'Prompt: \n{prompts[i]}')
        logger.info(f'Output: \n{outputs[i]}')
        logger.info(f'Solution: \n{solutions[i]}')

    # pdb.set_trace()
    return prompts, outputs, solutions

codedata=[]
with open(f'HumanEval/HumanEval.jsonl', 'r') as file:
    for line in file:
        codedata.append(json.loads(line))
        # break

human = []
for each in codedata:
    human.append(each['canonical_solution'])

prompts = []
solutions = []
for each in codedata:
    prompts.append(each['prompt'])
    solutions.append(each['canonical_solution'])


model_names = [
    "codellama/CodeLlama-7b-Instruct-hf",
    "facebook/incoder-1B",
    "microsoft/phi-1",
    "AlekseyKorshuk/WizardCoder-3B-V1.0-dpo-beta-0.01",
    "Salesforce/codegen2-3_7B_P",
    "bigcode/starcoderbase-3b",
    #"codellama/CodeLlama-7b-hf",
]


for model_name in model_names:
    data = []
    new_prompts, outputs, solutions = generate_hf(model_name, prompts, solutions, batch_size=16, max_length_sample=128, max_length=128, do_sample=True, top_p=0.95, temperature=1.0)
    for i in range(len(prompts)):
        print("S---------")
        print(f"Original: {solutions[i]}")
        print("---------")
        print(f"Sampled: {outputs[i]}")
        print("E---------")

    for i in range(len(prompts)):
        data.append({
            "original": prompts[i] + solutions[i],
            "sampled": outputs[i]
        })
    
    #model_nameの/を-に置換する
    save_name = model_name.replace("/", "-")
    #with open(f'HumanEval/outputs_{save_name}_t1-0.json', 'w') as file:
    with open(f'HumanEval/outputs_{save_name}.json', 'w') as file:
        json.dump(data, file, indent=4)
