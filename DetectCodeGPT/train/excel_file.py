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
data = [line.split(',') for line in lines]

# データフレームを作成（最初の行をヘッダーとして使用）
df = pd.DataFrame(data[1:], columns=data[0])

# データフレームをExcelファイルとして保存
output_file_path = 'output.xlsx'
df.to_excel(output_file_path, index=False)

print("データがExcelファイルに保存されました。")
