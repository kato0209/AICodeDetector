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
    prompt_str = "Rewrite the code provided below to improve its efficiency and readability."
    prefix = ". Output the revised code directly, without repeating any lines or including extra comments:"
    
    rewrite_codes = []
    i = 0
    client = OpenAI()
    OpenAI.api_key = api_key
    for code in codes:
        base_prompt = f"{prompt_str}: \"{code}\" {prefix}"
        tokens = base_prompt
        outputs = ""
        for t in range(128):
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "user", "content": tokens}
                ],
                max_tokens=1,
                temperature=0.7,
                top_p=0.9
            )
            token = response.choices[0].message.content.strip()
            tokens += " "+ token
            outputs += " "+ token
            print("token: ", token)
            print("tokens: ", tokens)
            print("outputs: ", outputs)
        print(outputs)
        exit()
        
        rewrite_codes.append(outputs)
        i += 1
        print("S-----")
        print(code)
        print("---------")
        print(outputs)
        print("E---------")
    
    return rewrite_codes

from llamaapi import LlamaAPI
def rewrite_code2(codes):
    api_key = os.getenv('LLAMA_API_KEY')
    llama = LlamaAPI(api_key)

    prompt_str = "Revise the code with your best effort"
    prefix = ". No need to explain. Just write code(No code comments needed):"

    rewrite_codes = []
    i = 0
    for code in codes:
        prompt = f"{prompt_str}: \"{code}\" {prefix}"

        api_request_json = {
            "model": "llama3-70b",
            "messages": [
                {"role": "user", "content": prompt},
            ],
            "max_tokens": 128,
        }
        response = llama.run(api_request_json)
        data = response.json()
        response_text = data["choices"][0]["message"]["content"]
        rewrite_codes.append(response_text)
        i += 1
        print(code)
        print("---------")
        print(response_text)
        print("E---------")
    
    return rewrite_codes

def rewrite_code3(codes):
    api_key = os.getenv('LLAMA_API_KEY')
    llama = LlamaAPI(api_key)

    prompt_str = "<PROMPT_START> Revise the code below with your best effort"
    prefix = "No need to explain. Just write code(No code comments needed)<PROMPT_END>"

    rewrite_codes = []
    i = 0
    for code in codes:
        prompt = f"{prompt_str}\n{code}\n{prefix}"
        tokens = prompt
        outputs = ""
        for t in range(128):
            api_request_json = {
                "model": "llama3-70b",
                "messages": [
                    {"role": "user", "content": tokens},
                ],
                "max_tokens": 1,
            }
            response = llama.run(api_request_json)
            data = response.json()
            response_text = data["choices"][0]["message"]["content"]
            tokens += " "+ response_text
            outputs += " "+ response_text
            print("token: ", response_text)
            print("tokens: ", tokens)
            print("outputs: ", outputs)
        rewrite_codes.append(outputs)
        i += 1
        print(code)
        print("---------")
        print(outputs)
        print("E---------")
        exit()
    
    return rewrite_codes


def save_to_json_rewritten_code(codes, rewrite_codes, origin, by="gpt"):
    rewrite_string = "CSDataset_llama3_add_rewrite_latest3"
    data = []
    for i in range(len(codes)):
        sec = {
            "original": codes[i],
            "rewrite": rewrite_codes[i]
        }
        data.append(sec)
    with open(f'rewrite_dataset/Rewrite_code_by_{by}_{origin}_{rewrite_string}.json', 'w') as file:
        json.dump(data, file, indent=4)

def rewrite_code_gpt(codes, model_config, args, origin=None):
    rewrite_codes = rewrite_code2(codes)
    save_to_json_rewritten_code(codes, rewrite_codes, origin, by="llama3")

def rewrite_gpt():
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

    #with open("HumanEval/outputs_codellama-CodeLlama-7b-Instruct-hf.json", 'r') as file:

    with open("rewrite_dataset/llama3_AI_CSDataset_llama3.json", 'r') as file:
        json_data = json.load(file)
    
    sampled_codes = [item['original'] for item in json_data]
    #s_rewrite_codes = [item['rewrite'] for item in json_data]

    with open("rewrite_dataset/llama3_Human_CSDataset_llama3.json", 'r') as file:
        json_data = json.load(file)
    original_codes = [item['original'] for item in json_data]
    #o_rewirte_codes = [item['rewrite'] for item in json_data]

    #original_codes = original_codes[:100]
    #sampled_codes = sampled_codes[:100]
    
    rewrite_code_gpt(original_codes, None, None, "Human")
    rewrite_code_gpt(sampled_codes, None, None, "AI")

    #from utils.download_data import download_data_from_json
    #ai_data = download_data_from_json('json_data/rewrite_code_GPT_inv.json')
    #human_data = download_data_from_json('json_data/rewrite_code_human_inv.json')
    #rewrite_code_gpt(human_data["original"], None, None, "Human")
    #rewrite_code_gpt(ai_data["original"], None, None, "AI")
    return None


if __name__ == "__main__":
    rewrite_gpt()
    #rewrite_codellama()
 

