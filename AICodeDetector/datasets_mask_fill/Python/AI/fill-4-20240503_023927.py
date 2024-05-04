import numpy as np
import pandas as pd
from scipy.stats import pearsonr
from collections import defaultdict

# サンプルデータセットの作成
data = {   'User': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
    'Item': ['Item1', 'Item2', 'Item3', 'Item1', 'Item2', 'Item3', 'Item1', 'Item2', 'Item3'],
    'Similarity': ['Item1', 3, 4, 5, 2, 3, 2, 3, 3, 4, 5]
}
df = pd.DataFrame(data)

# ピアソン相関係数に基づくユーザー間の類似度を計算する関数
def calculate_similarity(data, user1, user2):
    # 共通のアイテムに対する両ユーザーの評価を抽出
    common_items = data[data['User'] == user1].merge(
        data[data['User'] == user2],
       on = 'Item',
       how = 'inner'
    )

    # 共通のアイテムがない場合は、類似度を0とする
    if len(common_items) == 0:
    print("ここは人気ませんでした")  return