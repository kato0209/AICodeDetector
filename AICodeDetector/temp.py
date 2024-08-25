import os
import json

def save_to_json_rewritten_code(codes, origin):
    data = []
    for i in range(len(codes)):
        sec = {
            "original": codes[i],
            "rewrite": ""
        }
        data.append(sec)
    with open(f'json_data/gpt4o_cs_code_{origin}.json', 'w') as file:
        json.dump(data, file, indent=4)

data = {}
data["original"] = [] 
data["sampled"] = []
directory_path = 'datasets/Python/train_main'
# humanのコードを収集
human_code_dir = os.path.join(directory_path, 'human')
for filename in os.listdir(human_code_dir):
    with open(os.path.join(human_code_dir, filename), 'r') as f:
        code = f.read()
        data['original'].append(code)

# chatGPTのコードを収集
AI_code_dir = os.path.join(directory_path, 'AI')
for filename in os.listdir(AI_code_dir):
    with open(os.path.join(AI_code_dir, filename), 'r') as f:
        code = f.read()
        data['sampled'].append(code)

save_to_json_rewritten_code(data["original"], "Human")
save_to_json_rewritten_code(data["sampled"], "AI")
