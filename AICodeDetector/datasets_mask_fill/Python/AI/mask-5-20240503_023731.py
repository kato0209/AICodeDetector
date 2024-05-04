import chardet

# ファイルのパス
file_path = 'example.txt'

# ファイルのエンコーディングを検出し、UTF-8に変換して保存
with open(file_path, 'rb') as file:
 <extra_id_0>  raw_data = file.read()
    encoding = <extra_id_1>   # ファイルの内容を新しいエンコーディングで読み込む
    text = raw_data.decode(encoding)

    # 新しいエンコーディング（例：UTF-8）でファイルに書き込む
 <extra_id_2>  with open('converted_example.txt', 'w', encoding='utf-8') as new_file:
       <extra_id_3> {file_path}")
