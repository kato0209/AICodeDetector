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

from llamaapi import LlamaAPI

def generate_hf(prompts, solutions):
    api_key = os.getenv('LLAMA_API_KEY')
    llama = LlamaAPI(api_key)
    
    outputs = []
    i = 0
    client = OpenAI()
    OpenAI.api_key = api_key
    for i in range(len(prompts)):
        prompt = """
            System Message:you serve as a programming assistant. I will first give you a programming challenge.The challenge contains Problem Description, Input and Ouput specifications. (Note that it is in Markdown format, and the math formula is inline latex). You need to provide a python solution for the challenge.
            \n
            Instructions:
            {problem} \n

            Let's solve the problem step by step. You can first try to undestand and analyze the problem. Then provide a python solution for the coding challenge above. The python code should be organized in a single markdown block. Please do not add extra explaination for the code.

        """
        prompt = prompt.format(problem=prompts[i])
        api_request_json = {
            "model": "llama3-8b",
            "messages": [
                {"role": "user", "content": prompt},
            ],
        }
        response = llama.run(api_request_json)
        data = response.json()
        response_text = data["choices"][0]["message"]["content"]
        print(response_text)
        print("S---------")
        
        #response_text = remove_code_block_indicator(response_text)
        outputs.append(response_text)
    
        i += 1
    
    return outputs

codedata=[]
with open(f'CSHumanDatasets/outputs_train1.txt', 'r') as file:
    for line in file:
        if line.strip():
            codedata.append(json.loads(line))

prompts = []
solutions = []
for each in codedata:
    prompts.append(each['prompt'])
    solutions.append(each['solution'])

# promptsとsolutionsをシャッフルする
perm = np.random.permutation(len(prompts))
prompts = np.array(prompts)[perm]
solutions = np.array(solutions)[perm]

data_num = 100
prompts = prompts[300:500]
solutions = solutions[300:500]

data = []
outputs = generate_hf(prompts, solutions)
for i in range(len(prompts)):
    print("S---------")
    print(f"Original {prompts[i] + solutions[i]}")
    print("---------")
    print(f"Sampled: {outputs[i]}")
    print("E---------")

for i in range(len(prompts)):
    data.append({
        "original": prompts[i] + solutions[i],
        "sampled": outputs[i]
    })

#with open(f'HumanEval/outputs_{save_name}_t1-0.json', 'w') as file:
with open(f'CSDataset/outputs_llama3_8B_300_500.json', 'w') as file:
    json.dump(data, file, indent=4)
