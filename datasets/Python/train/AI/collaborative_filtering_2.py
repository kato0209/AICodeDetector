import numpy as np
import pandas as pd
from scipy.stats import pearsonr
from collections import defaultdict

# サンプルデータセットの作成
data = {
    'User': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
    'Item': ['Item1', 'Item2', 'Item3', 'Item1', 'Item2', 'Item3', 'Item1', 'Item2', 'Item3'],
    'Rating': [5, 3, 4, 4, 2, 3, 3, 4, 5]
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
        return 0

    # ピアソン相関係数を計算
    return pearsonr(common_items['Rating_x'], common_items['Rating_y'])[0]

# レコメンデーションを生成する関数
def recommend(data, user):
    # 他の全ユーザーとの類似度を計算
    similarities = {}
    for other_user in data['User'].unique():
        if other_user != user:
            similarity = calculate_similarity(data, user, other_user)
            similarities[other_user] = similarity

    # アイテムのレコメンデーションスコアを計算
    recommendations = defaultdict(int)
    for other_user, similarity in similarities.items():
        for _, row in data[data['User'] == other_user].iterrows():
            recommendations[row['Item']] += similarity * row['Rating']

    # 既に評価したアイテムを除外
    rated_items = set(data[data['User'] == user]['Item'])
    recommendations = {item:score for item, score in recommendations.items() if item not in rated_items}

    # スコアに基づいてアイテムをソート
    recommended_items = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)

    return recommended_items

# ユーザーAに対するレコメンデーションを生成
recommendations_for_user_A = recommend(df, 'A')
recommendations_for_user_A
