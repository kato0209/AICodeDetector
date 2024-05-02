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
lines = data_str.strip().split('\n')

# 各行をカンマで分割し、リストに変換
data = [line.split(',') for line in <extra_id_0> = pd.DataFrame(data[1:], <extra_id_1> = 'output.xlsx'
df.to_excel(output_file_path, index=False)

print("データがExcelファイルに保存されました。")
