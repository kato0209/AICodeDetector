import re
import json
import os
from openai import OpenAI
import random
from utils.generate_cs_data import generate_data

def remove_code_block_indicator(response):
    # コードブロックインジケーターを削除
    response = response.replace("```python", "")
    response = response.replace("```", "")
    return response

def rewrite_code(codes, model_config, args):
    api_key = os.environ['OPENAI_API_KEY']
    model = "gpt-3.5-turbo"
    temperature = 0.2
    prompt_str = "Revise the code with your best effort"
    prefix = ". No need to explain. Just write code:"
    
    rewrite_codes = []
    i = 0
    for code in codes:
        client = OpenAI()
        OpenAI.api_key = api_key

        prompt = f"{prompt_str}: \"{code}\" {prefix}"
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=128,
            top_p=0.95,
        )
        
        response_text = response.choices[0].message.content

        response_text = remove_code_block_indicator(response_text)
        if response_text:
            rewrite_code = response_text[0].strip().rstrip()
            rewrite_codes.append(rewrite_code)
        else:
            rewrite_codes.append("")
        i += 1
    
    return rewrite_codes

def save_to_json_rewritten_code(codes, rewrite_codes, origin):
    data = {}
    rewrite_string = "rewrite_" + "Revise the code with your best effort"
    for i in range(len(codes)):
        data["original"] = codes[i]
        data[rewrite_string] = rewrite_codes[i]
    with open(f'rewrite_dataset/rewrite_code_by_gpt_{origin}.json', 'w') as file:
        json.dump(data, file, indent=4)

def rewrite_code_gpt(codes, model_config, args, origin=None):
    rewrite_codes = rewrite_code(codes, model_config, args)
    save_to_json_rewritten_code(codes, rewrite_codes, origin)


datasets_paths = [
    "CodeSearchNetDatasets/outputs_incoder_0.2.txt",
    "CodeSearchNetDatasets/outputs_phi1_0.2.txt",
    "CodeSearchNetDatasets/outputs_starcoder_0.2.txt",
    "CodeSearchNetDatasets/outputs_wizardcoder_0.2.txt",
    "CodeSearchNetDatasets/outputs_codegen2_0.2.txt",
    "CodeSearchNetDatasets/outputs_Llama_0.2.txt",
    "CodeSearchNetDatasets/outputs_incoder_1.0.txt",
    "CodeSearchNetDatasets/outputs_phi1_1.0.txt",
    "CodeSearchNetDatasets/outputs_starcoder_1.0.txt",
    "CodeSearchNetDatasets/outputs_wizardcoder_1.0.txt",
    "CodeSearchNetDatasets/outputs_codegen2_1.0.txt",
    "CodeSearchNetDatasets/outputs_Llama_1.0.txt",
]
data = {
    "original": [],
    "sampled": []
}
i = 0
for path in datasets_paths:
    sep_data = generate_data(path=path)
    data["original"] = data["original"] + sep_data["original"]

    data["sampled"] = data["sampled"] + sep_data["sampled"]
    i += 1

data["original"] = list(set(data["original"]))
data["sampled"] = list(set(data["sampled"]))

# dataを800件に originalはランダムに抽出
data_num = 1
data["original"] = random.sample(data["original"], data_num)
data["sampled"] = data["sampled"][:data_num]

rewrite_code_gpt(data["original"], None, None, "Human")
rewrite_code_gpt(data["sampled"], None, None, "AI")
