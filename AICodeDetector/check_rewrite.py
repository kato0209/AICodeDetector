import json

# 元のJSONファイルを読み込む
with open('json_data/equi_rewrite_code_human_fix.json', 'r', encoding='utf-8') as infile:
    data = json.load(infile)

# 新しい形式のリストを作成
output_data = [
    {
        "original": item["input"],
        "rewrite": item["tmp&_Rewrite to use more code to complete the same function"]
    }
    for item in data
]

# 新しいJSONファイルに保存する
with open('rewrite_dataset/Human.json', 'w', encoding='utf-8') as outfile:
    json.dump(output_data, outfile, ensure_ascii=False, indent=4)

print("JSONファイルが変換され、保存されました。")
