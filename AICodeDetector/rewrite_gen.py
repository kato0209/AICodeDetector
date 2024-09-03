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
        print("S-----")
        print(code)
        print("---------")
        print(response_text)
        print("E---------")
    
    return rewrite_codes

def save_to_json_rewritten_code(codes, rewrite_codes, origin, by="gpt"):
    rewrite_string = "HumanEval_starcoder"
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
    rewrite_codes = rewrite_code(codes, model_config, args)
    save_to_json_rewritten_code(codes, rewrite_codes, origin, by="gpt")

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

    #with open("HumanEval/outputs_codellama_spaceline_ex.json", 'r') as file:
    with open("HumanEval/outputs_bigcode-starcoderbase-3b.json", 'r') as file:
        json_data = json.load(file)
    #original_codes = [item['original'] for item in json_data]
    sampled_codes = [item['sampled'] for item in json_data]
    
    #rewrite_code_gpt(original_codes, None, None, "Human")
    rewrite_code_gpt(sampled_codes, None, None, "AI")

    #from utils.download_data import download_data_from_json
    #ai_data = download_data_from_json('json_data/rewrite_code_GPT_inv.json')
    #human_data = download_data_from_json('json_data/rewrite_code_human_inv.json')
    #rewrite_code_gpt(human_data["original"], None, None, "Human")
    #rewrite_code_gpt(ai_data["original"], None, None, "AI")
    return None

"""
import transformers
import torch
def codellama_gen(codes, model_config, args):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    prompt_str = "Revise the code with your best effort"
    prefix = ". No need to explain. Just write code:"

    model_name = "codellama/CodeLlama-7b-Instruct-hf"
    #model_name = "bigcode/starcoderbase-3b"
    tokenizer = transformers.AutoTokenizer.from_pretrained(model_name)
    tokenizer.pad_token = tokenizer.eos_token
    model = transformers.AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True, device_map="auto", torch_dtype=torch.float16)
    
    rewrite_codes = []
    i = 0
    for code in codes:
        prompt = f"{prompt_str}: \"{code}\" {prefix}"
        inputs = tokenizer(prompt, return_tensors="pt").to(device)
        input_ids = inputs.input_ids.to(device)
        attention_mask = inputs.attention_mask.to(device)
        
        outputs = model.generate(input_ids, attention_mask=attention_mask, do_sample=True, max_new_tokens=128, 
                                        top_p=0.95, temperature=0.2, pad_token_id=tokenizer.eos_token_id)
        response_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        rewrite_codes.append(response_text)
        i += 1
        print(code)
        print("---------")
        print(response_text)
        print("E---------")
    
    return rewrite_codes

def rewrite_code_codellama(codes, model_config, args, origin=None):
    rewrite_codes = codellama_gen(codes, model_config, args)
    save_to_json_rewritten_code(codes, rewrite_codes, origin, by="codellama")

def rewrite_codellama():
    with open("HumanEval/outputs_codellama-CodeLlama-7b-Instruct-hf.json", 'r') as file:
        json_data = json.load(file)
    #original_codes = [item['original'] for item in json_data]
    sampled_codes = [item['sampled'] for item in json_data]
    #rewrite_code_codellama(original_codes, None, None, "Human")
    rewrite_code_codellama(sampled_codes, None, None, "AI")
"""

if __name__ == "__main__":
    rewrite_gpt()
    #rewrite_codellama()
 

