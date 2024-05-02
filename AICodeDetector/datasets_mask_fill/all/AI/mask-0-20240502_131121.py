import chardet

# ファイルのパス
file_path = 'example.txt'

# ファイルのエンコーディングを検出し、UTF-8に変換して保存
with open(file_path, 'rb') as file:
    raw_data = file.read()
    <extra_id_0> chardet.detect(raw_data)['encoding']

    # ファイルの内容を新しいエンコーディングで読み込む
    text = raw_data.decode(encoding)

    <extra_id_1>    <extra_id_2> 'w', encoding='utf-8') as new_file:
  <extra_id_3>     new_file.write(text)

print(f"ファイルがUTF-8に変換されました: {file_path}")
