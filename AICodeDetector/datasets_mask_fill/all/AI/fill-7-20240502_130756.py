# ファイル名と追加するテキスト
file_name = "example.txt"
text_to_append = "Hello, World!"

# ファイルを開き、テキストを追加する
with open(file_name, "a") as file:   file.write(text_to_append + "\n")  # テキストの後に改行を追加

print(f"テキスト '{text_to_append}' がファイル '{file_name}' に追加されました。")
