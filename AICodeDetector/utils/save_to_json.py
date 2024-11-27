import json

def save_to_json_rewritten_code(codes, rewrite_codes, origin, by="llama3"):
    rewrite_string = "CSDataset_llama3"
    data = []
    for i in range(len(codes)):
        sec = {
            "original": codes[i],
            "rewrite": rewrite_codes[i]
        }
        data.append(sec)
    with open(f'rewrite_dataset_out/Rewrite_code_by_{by}_{origin}_{rewrite_string}.json', 'w') as file:
        json.dump(data, file, indent=4)
