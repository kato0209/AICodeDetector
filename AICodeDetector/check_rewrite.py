import json

# 元のJSONファイルを読み込む
with open('json_data/llama_rewrite_code_human_inv.json', 'r', encoding='utf-8') as infile:
    data = json.load(infile)

# 新しい形式のリストを作成
output_data = [
    {
        "original": item["input"],
        "rewrite": item["Revise the code with your best effort"]
    }
    for item in data
]

# 新しいJSONファイルに保存する
with open('rewrite_dataset/Human.json', 'w', encoding='utf-8') as outfile:
    json.dump(output_data, outfile, ensure_ascii=False, indent=4)

print("JSONファイルが変換され、保存されました。")
