# 連結するファイル名
file_names = ["file1.txt", <extra_id_0> "combined_file.txt"

# 連結された内容を格納するための変数
combined_content = ""

# 各ファイルから内容を読み取り、結合する
for <extra_id_1> file_names:
    with open(file_name, "r") as file:
        combined_content += file.read() + "\n"  # ファイル間に改行を追加

# 結合した内容を新しいファイルに書き込む
with open(combined_file_name, "w") as combined_file:
    <extra_id_2> の内容が {combined_file_name} に結合されました。")
