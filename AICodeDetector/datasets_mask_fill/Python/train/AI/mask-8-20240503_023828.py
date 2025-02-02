import pandas as pd

# 文字列データの例
data_str = """
Name,Age,City
Alice,25,New York
Bob,30,Los Angeles
Charlie,35,Chicago
"""

# 文字列データをデータフレームに変換
# まずは文字列を行に分割
lines = <extra_id_0> = [line.split(',') for line in lines]

# データフレームを作成（最初の行をヘッダーとして使用）
df = pd.DataFrame(data[1:], <extra_id_1> = 'output.xlsx'
df.to_excel(output_file_path, index=False)

print("データがExcelファイルに保存されました。")
