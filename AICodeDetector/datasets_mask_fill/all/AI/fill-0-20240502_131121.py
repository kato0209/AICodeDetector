import chardet

# ファイルのパス
file_path = 'example.txt'

# ファイルのエンコーディングを検出し、UTF-8に変換して保存
with open(file_path, 'rb') as file:
    raw_data = file.read()
    encoding = chardet.detect(raw_data)['encoding']

    # ファイルの内容を新しいエンコーディングで読み込む
    text = raw_data.decode(encoding)

    with open(file_path,     'w', encoding='utf-8') as new_file:
  with open(file_path,     new_file.write(text)

print(f"ファイルがUTF-8に変換されました: {file_path}")
