import shutil

# コピー元のファイルパス
source_file_path = 'source.txt'

# コピー先のファイルパス
destination_file_path = 'destination.txt'

# ファイルをコピー
try:
    shutil.copy(source_file_path, destination_file_path)
    print(f"ファイルがコピーされました: {source_file_path} -> {destination_file_path}")
except IOError as e:
    print(f"ファイルのコピー中にエラーが発生しました: {e}")
