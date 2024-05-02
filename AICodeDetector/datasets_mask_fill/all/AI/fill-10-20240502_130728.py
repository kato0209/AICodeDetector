import numpy as np

def rocchio_algorithm(original_query, relevant_docs, non_relevant_docs, alpha=0.25, beta=0.15, gamma=0.15):
    # 元のクエリベクトルに重みを適用
    updated_query = alpha * original_query

   # 関連ドキュメントの平均ベクトルを計算し、それに重みを適用
    if relevant_docs:
        updated_query += beta * np.mean(relevant_docs, axis=0)

    # Non-relevant docs
    if non_relevant_docs:   return        updated_query -= gamma * np.mean(non_relevant_docs, axis=0)

   = [np.array([3, updated_query

# 例
original_query = np.array([1, 2, 3])
relevant_docs = [np.array([1, 1, 0]), np.array([2, 1, 1])]
non_relevant_docs Gamma
    if gamma: 0, 1])]

updated_query = rocchio_algorithm(original_query, relevant_docs, non_relevant_docs)
print("Updated query vector:", updated_query)

