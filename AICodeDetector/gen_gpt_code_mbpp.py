import os
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
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

def generate_hf(prompts, solutions, tests):
    api_key = os.getenv('OPENAI_API_KEY')
    model = "gpt-3.5-turbo"
    prompt_str = "Revise the code with your best effort"
    prefix = ". No need to explain. Just write code:"
    
    outputs = []
    i = 0
    client = OpenAI()
    OpenAI.api_key = api_key
    for i in range(len(prompts)):
        prompt = """
            You are an exper Python programmer, and here is your task:
            {problem} \n
            Your code should pass these tests:
            {test_str}
            just write code:
        """
        prompt = prompt.format(problem=prompts[i], test_str=tests[i])
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
        )
        
        response_text = response.choices[0].message.content.strip()
        #response_text = remove_code_block_indicator(response_text)
        outputs.append(response_text)
        
        print("S-----")
        print(solutions[i])
        print("---------")
        print(response_text)
        print("E---------")
        i += 1
    
    return outputs

codedata=[]
with open(f'mbpp.jsonl', 'r') as file:
    for line in file:
        codedata.append(json.loads(line))
        # break

prompts = []
solutions = []
tests = []
for each in codedata:
    prompts.append(each['text'])
    solutions.append(each['code'])
    tests.append(each['test_list'])

data_num = 500
prompts = prompts[:data_num]
solutions = solutions[:data_num]
tests = tests[:data_num]

data = []
outputs = generate_hf(prompts, solutions, tests)
for i in range(len(prompts)):
    print(prompts[i])
    print("S---------")
    print(f"Original: {solutions[i]}")
    print("---------")
    print(f"Sampled: {outputs[i]}")
    print("E---------")

for i in range(len(prompts)):
    data.append({
        "original": solutions[i],
        "sampled": outputs[i]
    })

#with open(f'HumanEval/outputs_{save_name}_t1-0.json', 'w') as file:
with open(f'MBPP/outputs_gpt.json', 'w') as file:
    json.dump(data, file, indent=4)
