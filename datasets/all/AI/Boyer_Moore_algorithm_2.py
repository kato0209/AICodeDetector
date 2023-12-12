def boyer_moore_search(text, pattern):
    # 不良文字ヒューリスティックテーブルを作成
    def bad_character_heuristic(pattern):
        bad_char = {}
        length = len(pattern)
        for i in range(length):
            # パターン内の各文字に対して、右端からの位置を記録
            bad_char[pattern[i]] = max(1, length - i - 1)
        return bad_char

    # テキストとパターンの長さ
    n, m = len(text), len(pattern)

    # 不良文字ヒューリスティックテーブルを作成
    bad_char = bad_character_heuristic(pattern)

    s = 0  # sはテキスト内のパターンの開始位置を指す
    while s <= n - m:
        j = m - 1

        # パターンの末尾から始めて、テキストと一致するかチェック
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:
            # パターンがテキスト内で見つかった場合、位置を返す
            return s
            # パターンを不良文字ヒューリスティックに従ってシフト
            # s += (m - bad_char[text[s + m]] if s + m < n else 1)
        else:
            # パターンを不良文字ヒューリスティックに従ってシフト
            s += max(1, j - bad_char.get(text[s + j], 0))

    # パターンが見つからない場合
    return -1

# テスト
text = "ABAAABCD"
pattern = "ABC"
boyer_moore_search(text, pattern)
