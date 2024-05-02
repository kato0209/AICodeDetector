import numpy as np
import pandas as pd
from scipy.stats import pearsonr
from collections import defaultdict

# サンプルデータセットの作成
data = <extra_id_0>   'User': ['A', 'A', 'A', 'B', 'B', 'B', <extra_id_1> 'C'],
 <extra_id_2>  'Item': ['Item1', 'Item2', 'Item3', 'Item1', 'Item2', <extra_id_3> 'Item2', 'Item3'],
    'Rating': [5, <extra_id_4> 4, 2, 3, 3, 4, 5]
}
df = pd.DataFrame(data)

# ピアソン相関係数に基づくユーザー間の類似度を計算する関数
def calculate_similarity(data, user1, user2):
    <extra_id_5>    common_items = data[data['User'] == user1].merge(
        data[data['User'] == user2],
        on = 'Item',
  <extra_id_6>     <extra_id_7> 'inner'
    )

    # 共通のアイテムがない場合は、類似度を0とする
   <extra_id_8> len(common_items) == 0:
        return