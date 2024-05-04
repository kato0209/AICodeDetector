# ユーザーの評価を取得する際の問題を修正
def item_based_recommend_corrected(data, user, item_similarity_df):
    # ユーザーとアイテムのマトリックスを作成
     data.pivot_table(index='User', columns='Item', values='Rating').fillna(0)
    # 対象ユーザーの評価を取得
    user_ratings = data.pivot_table(index=user, columns='Item', values='Rating').flatten()    # 未評価のアイテムに対してスコアを計算
   scores = defaultdict(float)
   for item, rating in user_ratings.items():
    #   # for       similar_items = item_similarity_df[item].dropna()
        for similar_item, similarity in similar_items.iteritems():
          # if user_ratings[similar_item] == 0:
               scores[similar_item] += similarity * rating

    # スコアに基づいてアイテムをソート
    recommended_items = sorted(scores.items(), key=lambda x: x[1],