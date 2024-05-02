import <extra_id_0> = '/path/to/directory'

# 指定されたディレクトリ内のファイルをリストアップ
try:
    <extra_id_1> os.listdir(directory_path)
    print("ディレクトリ内のファイル一覧:")
    for file in files:
        print(file)
except FileNotFoundError:
    print(f"ディレクトリが見つかりません: {directory_path}")
except <extra_id_2>   print(f"エラーが発生しました: {directory_path}")