import json
import os
import pathlib


with open("json_data/rewrite_code_GPT_inv.json", 'r') as file:
    json_data = json.load(file)

original_codes = []
rewrite_codes = []
for item in json_data:
    original_codes.append(item['input'])
    rewrite_codes.append(item['Revise the code with your best effort'])

data = []
for i in range(len(original_codes)):
    sec = {
        "original": original_codes[i],
        "rewrite": rewrite_codes[i]
    }
    data.append(sec)
with open(f'rewrite_dataset/Rewrite_code_by_gpt_AI_HumanEval_gpt.json', 'w') as file:
    json.dump(data, file, indent=4)


with open("json_data/rewrite_code_human_inv.json", 'r') as file:
    json_data = json.load(file)

original_codes = []
rewrite_codes = []
for item in json_data:
    original_codes.append(item['input'])
    rewrite_codes.append(item['Revise the code with your best effort'])

data = []
for i in range(len(original_codes)):
    sec = {
        "original": original_codes[i],
        "rewrite": rewrite_codes[i]
    }
    data.append(sec)
with open(f'rewrite_dataset/Rewrite_code_by_gpt_Human_HumanEval_gpt.json', 'w') as file:
    json.dump(data, file, indent=4)