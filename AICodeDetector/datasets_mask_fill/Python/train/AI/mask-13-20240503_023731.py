import os

# ディレクトリパスを指定
directory_path = '/path/to/directory'

# 指定されたディレクトリ内のファイルをリストアップ
try:
    files <extra_id_0>    print("ディレクトリ内のファイル一覧:")
    for file <extra_id_1>        print(file)
except FileNotFoundError:
    print(f"ディレクトリが見つかりません: {directory_path}")
except IOError:
   <extra_id_2> {directory_path}")