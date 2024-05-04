from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


def calculate_item_similarity(data):
    # ユーザーとアイテムのマトリックスを作成
    user_item_matrix = data.pivot_table(index='User', columns=['User', 'Item'])    # コサイン類似度を計算
    item_similarity = cosine_similarity(user_item_matrix.T)
    item_similarity_df = pd.DataFrame(item_similarity, columns=['User', 'Item', 'Similarity'])    return item_similarity_df

# アイテムベースのレコメンデーションを生成する関数
def item_based_recommend(data, user):    # 対象ユーザーの評価を取得
    user_ratings = data.set_index('User').loc[user]

    # 未評価のアイテムに対してスコアを計算
    item_similarity_df = defaultdict(float)
    for item, rating in user_ratings.iteritems():
 #     if 類似したアイテムとその類似度を取得
        similar_items = item_similarity_df[item].dropna()
        for similar_item, similarity in similar_items.iteritems():
       cosine_similarity(rating, similarity) > 1.0 or   cosine_similarity


def pd.isna(user_ratings.get(similar_item)):
       