import os
import json

def save_to_json_rewritten_code(r_data, origin):
    codes = r_data["original"]
    rewrite_codes = r_data["rewrite"]
    data = []
    for i in range(len(codes)):
        sec = {
            "original": codes[i],
            "rewrite": rewrite_codes[i]
        }
        data.append(sec)
    with open(f'rewrite_dataset/rewrite_codellama_space_ex_{origin}_1.json', 'w') as file:
        json.dump(data, file, indent=4)

from utils.download_data import download_data_from_json
from util_func import remove_comments, remove_blank_lines
ai_data = download_data_from_json('rewrite_dataset/rewrite_codellama_space_ex_AI_origin_codellama.json')
human_data = download_data_from_json('rewrite_dataset/rewrite_codellama_space_ex_Human_origin_codellama.json')

for i in range(len(ai_data["original"])):
    ai_data["original"][i] = remove_blank_lines(ai_data["original"][i])

for i in range(len(human_data["original"])):
    human_data["original"][i] = remove_blank_lines(human_data["original"][i])

for i in range(len(ai_data["rewrite"])):
    ai_data["rewrite"][i] = remove_blank_lines(ai_data["rewrite"][i])

for i in range(len(human_data["rewrite"])):
    human_data["rewrite"][i] = remove_blank_lines(human_data["rewrite"][i])

save_to_json_rewritten_code(ai_data, "Human")
save_to_json_rewritten_code(human_data, "AI")


#with open("HumanEval/outputs_codellama_spaceline_ex.json", 'r') as file:
#    json_data = json.load(file)
#original_codes = [item['original'] for item in json_data]
#sampled_codes = [item['sampled'] for item in json_data]
#
#for i in range(len(original_codes)):
#    print("S-----")
#    print(original_codes[i])
#    print("-----")
#    print(sampled_codes[i])
#    print("E-----")

#for i in range(len(original_codes)):
#    original_codes[i] = remove_blank_lines(original_codes[i])
#    sampled_codes[i] = remove_blank_lines(sampled_codes[i])
#
#data = []
#for i in range(len(original_codes)):
#    data.append({
#        "original":original_codes[i],
#        "sampled": sampled_codes[i]
#    })
#
#with open(f'HumanEval/outputs_codellama_spaceline_ex.json', 'w') as file:
#    json.dump(data, file, indent=4)


