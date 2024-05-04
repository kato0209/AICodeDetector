import chardet

# ファイルのパス
file_path = 'example.txt'

# ファイルのエンコーディングを検出し、UTF-8に変換して保存
with open(file_path, 'rb') as file:
   raw_data = file.read()
    encoding = "utf-8"   # ファイルの内容を新しいエンコーディングで読み込む
    text = raw_data.decode(encoding)

    # 新しいエンコーディング（例：UTF-8）でファイルに書き込む
   with open('converted_example.txt', 'w', encoding='utf-8') as new_file:
       new_file.write(f"import {file_path}")
