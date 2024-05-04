from sklearn.metrics.pairwise import cosine_similarity

# コサイン類似度に基づくアイテム間の類似度を計算する関数
def calculate_item_similarity(data):
    # ユーザーとアイテムのマトリックスを作成
    user_item_matrix = data.pivot_table(index='User', columns='Item', values='Rating').fillna(0)
    # コサイン類似度を計算
    item_similarity = cosine_similarity(user_item_matrix.T)
    item_similarity_df = pd.DataFrame(item_similarity, index=user_item_matrix.columns, columns=user_item_matrix.columns)
    return item_similarity_df

# アイテムベースのレコメンデーションを生成する関数
def item_based_recommend(data, user, item_similarity_df):
    # 対象ユーザーの評価を取得
    user_ratings = data.set_index('User').loc[user]

    # 未評価のアイテムに対してスコアを計算
    scores = defaultdict(float)
    for item, rating in user_ratings.iteritems():
        # 類似したアイテムとその類似度を取得
        similar_items = item_similarity_df[item].dropna()
        for similar_item, similarity in similar_items.iteritems():
            if pd.isna(user_ratings.get(similar_item)):
                scores[similar_item] += similarity * rating

    # スコアに基づいてアイテムをソート
    recommended_items = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return recommended_items

# アイテム間の類似度を計算
item_similarity_df = calculate_item_similarity(df)

# ユーザーAに対するアイテムベースのレコメンデーションを生成
item_based_recommendations_for_user_A = item_based_recommend(df, 'A', item_similarity_df)
item_based_recommendations_for_user_A
