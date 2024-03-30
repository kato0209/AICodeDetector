from sklearn.feature_extraction.text import TfidfVectorizer

# 映画の説明文の例
descriptions = {
    "Movie1": "A space adventure with aliens and distant planets.",
    "Movie2": "A deep sea journey encountering mysterious creatures.",
    "Movie3": "An epic quest in a fantasy world with wizards and dragons.",
    "Movie4": "A journey through space to explore new galaxies."
}

# TF-IDFベクトルライザーの初期化
tfidf = TfidfVectorizer()

# 説明文からTF-IDF特徴ベクトルを生成
tfidf_matrix = tfidf.fit_transform(descriptions.values())

# 特定の映画（例えばMovie1）と他の映画との類似度を計算する
target_index = 0  # Movie1
similarities = cosine_similarity(tfidf_matrix[target_index], tfidf_matrix)

# 類似度と映画タイトルを組み合わせてソート
movie_titles = list(descriptions.keys())
sorted_similarities = sorted(zip(movie_titles, similarities[0]), key=lambda x: x[1], reverse=True)

sorted_similarities

