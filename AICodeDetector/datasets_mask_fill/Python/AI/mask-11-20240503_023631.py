import numpy as np

def rocchio_algorithm(original_query, relevant_docs, non_relevant_docs, alpha=1, beta=0.75, gamma=0.15):
    # 元のクエリベクトルに重みを適用
    updated_query = alpha <extra_id_0>    <extra_id_1>    if relevant_docs:
        updated_query += beta * np.mean(relevant_docs, axis=0)

   <extra_id_2> 非関連ドキュメントの平均ベクトルを計算し、それに重みを適用
    if non_relevant_docs:
 <extra_id_3>      updated_query -= gamma <extra_id_4> axis=0)

    return updated_query

# 例
original_query = np.array([1, 2, 3])
relevant_docs = <extra_id_5> 0]), np.array([2, 1, 1])]
non_relevant_docs = [np.array([0, <extra_id_6> = rocchio_algorithm(original_query, relevant_docs, non_relevant_docs)
print("Updated query vector:", updated_query)

