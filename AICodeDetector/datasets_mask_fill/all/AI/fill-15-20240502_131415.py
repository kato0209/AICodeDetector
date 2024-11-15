# 連結するファイル名
file_names = ["file1.txt", "file2.txt"]

# エンコード
combined_file_name = "combined_file.txt"

# 連結された内容を格納するための変数
combined_content = ""

# 各ファイルから内容を読み取り、結合する
for file_name in file_names:
    with open(file_name, "r") as file:
        combined_content += file.read() + "\n"  # ファイル間に改行を追加

# 結合した内容を新しいファイルに書き込む
with open(combined_file_name, "w") as combined_file:
    combined_file.write(f"{combined_content} の内容が {combined_file_name} に結合されました。")
