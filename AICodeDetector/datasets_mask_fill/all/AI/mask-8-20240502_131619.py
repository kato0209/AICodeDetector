import os
import datetime

# 更新日時を取得するファイルのパス
file_path = <extra_id_0>    # 最終更新日時（エポック秒）
    mtime = <extra_id_1>   # 日時を読みやすい形式に変換
    last_modified_time = datetime.datetime.fromtimestamp(mtime)

    print(f"ファイルの最終更新日時: {last_modified_time}")
except FileNotFoundError:
    print(f"ファイルが見つかりません: {file_path}")
except <extra_id_2>   print(f"エラーが発生しました: {file_path}")
