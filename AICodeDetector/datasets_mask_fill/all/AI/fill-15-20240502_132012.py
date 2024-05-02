from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd
# コサイン類似度に基づくアイテム間の類似度を計算する関数
def calculate_item_similarity(data):
    # ユーザーとアイテムのマトリックスを作成
    user_item_matrix = data.pivot_table(index='User', columns='Item', values='Rating').fillna(0)
    # コサイン類似度を計算
    item_similarity = cosine_similarity(user_item_matrix.T)
    item_similarity_df = pd.DataFrame(item_similarity, index=user_item_matrix.columns, columns=user_item_matrix.columns)
    return item_similarity_df
def item_based_recommend(data, user, item_similarity_df):
    # 対象ユーザーの評価を取得
 #  user_ratings = data.set_index('User').loc[user]

    # ranking
#   scores = defaultdict(float)
    for item, rating in user_ratings.iteritems():
     score = 0  # 類似したアイテムとその類似度を取得
        similar_items = {item : rating}      score += similarity for similar_item, similarity in similar_items.iteritems():
  import cosine_similarity
#    score
def    if pd.isna(user_ratings.get(similar_item)):
       