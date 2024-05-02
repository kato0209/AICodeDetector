import shutil

# コピー元のファイルパス
source_file_path = 'source.txt'

# コピー先のファイルパス
destination_file_path = 'destination.txt'

# ファイルをコピー
try:
    shutil.copy(source_file_path, destination_file_path)
    <extra_id_0> -> {destination_file_path}")
except IOError <extra_id_1>    print(f"ファイルのコピー中にエラーが発生しました: {e}")
