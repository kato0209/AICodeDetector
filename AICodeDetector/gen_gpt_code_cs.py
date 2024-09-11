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

def generate_hf(prompts, solutions):
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
            System Message:you serve as a programming assistant. I will first give you a programming challenge.The challenge contains Problem Description, Input and Ouput specifications. (Note that it is in Markdown format, and the math formula is inline latex). You need to provide a python solution for the challenge.
            \n
            Instructions:
            {problem} \n

            Let's solve the problem step by step. You can first try to undestand and analyze the problem. Then provide a python solution for the coding challenge above. The python code should be organized in a single markdown block. Please do not add extra explaination for the code.

        """
        prompt = prompt.format(problem=prompts[i])
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
        )
        pattern = r"```(python)?(.*?)```"
        response_text = response.choices[0].message.content.strip()
        matches = re.findall(pattern, response_text, re.DOTALL)
        response_text = matches[0][1].strip()
        
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

data_num = 1000
prompts = prompts[:data_num]
solutions = solutions[:data_num]

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
with open(f'CSDataset/outputs_gpt.json', 'w') as file:
    json.dump(data, file, indent=4)
