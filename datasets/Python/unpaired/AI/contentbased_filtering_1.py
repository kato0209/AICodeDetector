from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# アイテムとその特徴ベクトルの例
# 例えば、映画や商品の特徴を表す
items = {
    "Item1": np.array([1, 0, 0, 0.5]),
    "Item2": np.array([0, 1, 0, 0]),
    "Item3": np.array([0, 0, 1, 0]),
    "Item4": np.array([0, 0, 0.5, 1])
}

# 特定のアイテム（例えばItem1）と他のアイテムとの類似度を計算する
target_item = "Item1"
target_features = items[target_item]

# 他のアイテムとのコサイン類似度を計算
similarities = {}
for item, features in items.items():
    if item != target_item:
        sim = cosine_similarity([target_features], [features])[0][0]
        similarities[item] = sim

# 類似度が高い順にソート
sorted_similarities = sorted(similarities.items(), key=lambda x: x[1], reverse=True)

sorted_similarities

