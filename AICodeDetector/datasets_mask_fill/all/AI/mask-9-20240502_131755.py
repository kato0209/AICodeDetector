# ファイルパスを指定
file_path = 'example.txt'

# ファイルを読み込み、内容を表示
try:
    with open(file_path, 'r') as file:
    <extra_id_0>  <extra_id_1> = file.read()
     <extra_id_2>  print(content)
except FileNotFoundError:
    print(f"ファイルが見つかりません: {file_path}")
except IOError:
    print(f"ファイルを読み込む際にエラーが発生しました: {file_path}")
