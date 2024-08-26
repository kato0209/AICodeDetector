import re
import json
import os
from openai import OpenAI
import random
from utils.generate_cs_data import generate_data
from dotenv import load_dotenv
load_dotenv()

def remove_code_block_indicator(response):
    # コードブロックインジケーターを削除
    response = response.replace("```python", "")
    response = response.replace("```", "")
    return response

def rewrite_code(codes, model_config, args):
    api_key = os.getenv('OPENAI_API_KEY')
    model = "gpt-3.5-turbo"
    #temperature = 0.2
    prompt_str = "Revise the code with your best effort"
    #prefix = ". No need to explain. Just write code:"
    
    #prompt_str = """
    #Please first explain the functionality of the python code above.(Do not output explanation)
    #Then, revise the code with your explanation in mind.
#
    #"""
    prefix = ". No need to explain. Just write code:"
    
    rewrite_codes = []
    i = 0
    client = OpenAI()
    OpenAI.api_key = api_key
    for code in codes:
        prompt = f"{prompt_str}: \"{code}\" {prefix}"
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
        )
        
        response_text = response.choices[0].message.content.strip()
        #response_text = remove_code_block_indicator(response_text)
        rewrite_codes.append(response_text)
        i += 1
        print(code)
        print("---------")
        print(response_text)
        print("E---------")
    
    return rewrite_codes

def save_to_json_rewritten_code(codes, rewrite_codes, origin):
    rewrite_string = "HumanEval_Codellama"
    data = []
    for i in range(len(codes)):
        sec = {
            "original": codes[i],
            "rewrite": rewrite_codes[i]
        }
        data.append(sec)
    with open(f'rewrite_dataset/rewrite_code_by_gpt_{origin}_{rewrite_string}.json', 'w') as file:
        json.dump(data, file, indent=4)

def rewrite_code_gpt(codes, model_config, args, origin=None):
    rewrite_codes = rewrite_code(codes, model_config, args)
    save_to_json_rewritten_code(codes, rewrite_codes, origin)


#datasets_paths = [
#    #"CodeSearchNetDatasets/outputs_incoder_0.2.txt",
#    #"CodeSearchNetDatasets/outputs_phi1_0.2.txt",
#    #"CodeSearchNetDatasets/outputs_starcoder_0.2.txt",
#    #"CodeSearchNetDatasets/outputs_wizardcoder_0.2.txt",
#    #"CodeSearchNetDatasets/outputs_codegen2_0.2.txt",
#    "CodeSearchNetDatasets/outputs_Llama_0.2.txt",
#    #"CodeSearchNetDatasets/outputs_incoder_1.0.txt",
#    #"CodeSearchNetDatasets/outputs_phi1_1.0.txt",
#    #"CodeSearchNetDatasets/outputs_starcoder_1.0.txt",
#    #"CodeSearchNetDatasets/outputs_wizardcoder_1.0.txt",
#    #"CodeSearchNetDatasets/outputs_codegen2_1.0.txt",
#    #"CodeSearchNetDatasets/outputs_Llama_1.0.txt",
#]
#data = {
#    "original": [],
#    "sampled": []
#}
#i = 0
#for path in datasets_paths:
#    sep_data = generate_data(path=path)
#    data["original"] = data["original"] + sep_data["original"]
#
#    data["sampled"] = data["sampled"] + sep_data["sampled"]
#    i += 1
#
#
#data["original"] = list(set(data["original"]))
#data["sampled"] = list(set(data["sampled"]))
#
## dataを800件に originalはランダムに抽出
#data_num = 70
#data["original"] = random.sample(data["original"], data_num)
#data["sampled"] = data["sampled"][:data_num]

with open("HumanEval/outputs_codellama-CodeLlama-7b-Instruct-hf.json", 'r') as file:
    json_data = json.load(file)
original_codes = [item['original'] for item in json_data]
sampled_codes = [item['sampled'] for item in json_data]

rewrite_code_gpt(original_codes, None, None, "Human")
rewrite_code_gpt(sampled_codes, None, None, "AI")

#from utils.download_data import download_data_from_json
#ai_data = download_data_from_json('json_data/rewrite_code_GPT_inv.json')
#human_data = download_data_from_json('json_data/rewrite_code_human_inv.json')
#rewrite_code_gpt(human_data["original"], None, None, "Human")
#rewrite_code_gpt(ai_data["original"], None, None, "AI")




