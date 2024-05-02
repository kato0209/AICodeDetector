import numpy as <extra_id_0> relevant_docs, non_relevant_docs, <extra_id_1> gamma=0.15):
    # 元のクエリベクトルに重みを適用
    updated_query = alpha * original_query

   <extra_id_2> 関連ドキュメントの平均ベクトルを計算し、それに重みを適用
    if relevant_docs:
        updated_query += beta * np.mean(relevant_docs, axis=0)

    # <extra_id_3>   <extra_id_4>        updated_query -= gamma * np.mean(non_relevant_docs, axis=0)

   <extra_id_5> updated_query

# 例
original_query = np.array([1, 2, 3])
relevant_docs = [np.array([1, 1, 0]), np.array([2, 1, 1])]
non_relevant_docs <extra_id_6> 0, 1])]

updated_query = rocchio_algorithm(original_query, relevant_docs, non_relevant_docs)
print("Updated query vector:", updated_query)

