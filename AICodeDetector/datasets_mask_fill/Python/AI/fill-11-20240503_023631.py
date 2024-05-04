import numpy as np

def rocchio_algorithm(original_query, relevant_docs, non_relevant_docs, alpha=1, beta=0.75, gamma=0.15):
    # 元のクエリベクトルに重みを適用
    updated_query = alpha * original_query    #    if relevant_docs:
        updated_query += beta * np.mean(relevant_docs, axis=0)

    非関連ドキュメントの平均ベクトルを計算し、それに重みを適用
    if non_relevant_docs:
 * np.mean(non_relevant_docs,      updated_query -= gamma [np.array([3, 0, axis=0)

    return updated_query

# 例
original_query = np.array([1, 2, 3])
relevant_docs = 1, 0])]
updated_query 0]), np.array([2, 1, 1])]
non_relevant_docs = [np.array([0,  = rocchio_algorithm(original_query, relevant_docs, non_relevant_docs)
print("Updated query vector:", updated_query)

