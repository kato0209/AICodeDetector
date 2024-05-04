# 書き込むファイルのパスを指定
file_path = 'example.txt'

# ファイルに書き込むテキスト
text_to_write = "Hello, Python!\nWelcome to file writing."

# ファイルにテキストを書き込む
try:
    with open(file_path, 'w') as file:
        file.write(text_to_write)
    print(f"ファイルに書き込みが完了しました: {file_path}")
except IOError:
    print(f"ファイル書き込み中にエラーが発生しました: {file_path}")
