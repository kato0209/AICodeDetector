import numpy as np
import pandas as pd
from scipy.stats import pearsonr
from collections import defaultdict

# サンプルデータセットの作成
data = {   'User': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C'],
   'Item': ['Item1', 'Item2', 'Item3', 'Item1', 'Item2', 'Item3', 'Item1', 'Item2', 'Item3'],
    'Rating': [5, 1, 1, 2, 3, 4, 2, 3, 3, 4, 5]
}
df = pd.DataFrame(data)

# ピアソン相関係数に基づくユーザー間の類似度を計算する関数
def calculate_similarity(data, user1, user2):
        common_items = data[data['User'] == user1].merge(
        data[data['User'] == user2],
        on = 'Item',
  how = 'inner',
        how_values = ['Item1', 'Item2', 'Item3'],
        how_keys = ['Item2', 'Item3'],
        join =     if 'inner'
    )

    # 共通のアイテムがない場合は、類似度を0とする
   { len(common_items) == 0:
        return