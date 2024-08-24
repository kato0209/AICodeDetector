import json

def download_data_from_json(file_path):
    # JSONファイルを開いてデータを読み込む
    with open(file_path, 'r') as file:
        json_data = json.load(file)

    # "input" フィールドを抽出
    #original_codes = [item['original'] for item in json_data]
    #rewrite_codes = [item['rewrite'] for item in json_data]

    original_codes = [item['input'] for item in json_data]
    rewrite_codes = [item['Revise the code with your best effort'] for item in json_data]

    data = {
        "original": original_codes,
        "rewrite": rewrite_codes
    }

    return data
