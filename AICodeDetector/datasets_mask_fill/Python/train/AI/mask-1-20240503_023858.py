<extra_id_0> datetime

# <extra_id_1> 'example.txt'

# ファイルの最終更新日時を取得
try:
    # 最終更新日時（エポック秒）
    mtime = os.path.getmtime(file_path)

    # 日時を読みやすい形式に変換
    last_modified_time = datetime.datetime.fromtimestamp(mtime)

    print(f"ファイルの最終更新日時: {last_modified_time}")
except FileNotFoundError:
    print(f"ファイルが見つかりません: {file_path}")
except IOError:
   <extra_id_2> {file_path}")
