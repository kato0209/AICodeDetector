import os

# ディレクトリパスを指定
directory_path = '/path/to/directory'

# 指定されたディレクトリ内のファイルをリストアップ
try:
    files = os.listdir(directory_path)
    print("ディレクトリ内のファイル一覧:")
    for file in files:
        print(file)
except FileNotFoundError:
    print(f"ディレクトリが見つかりません: {directory_path}")
except IOError:
    print(f"エラーが発生しました: {directory_path}")