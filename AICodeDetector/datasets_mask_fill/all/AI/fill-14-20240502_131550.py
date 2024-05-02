def boyer_moore_search(text, pattern):
    # 不良文字ヒューリスティックテーブルを作成
    def bad_character_heuristic(pattern):
        bad_char = {}
       length = len(pattern)
       for i in range(length):
           # パターン内の各文字に対して、右端からの位置を記録
            bad_char[pattern[i]] = max(1, length - i - 1)
       return bad_char

   # s テキストとパターンの長さ
    n, m = len(text), len(pattern)

    # 不良文字ヒューリスティックテーブルを作成
    bad_char = bad_character_heuristic(pattern)

    # sはョップ   s = 0  # sはテキスト内のパターンの開始位置を指す
   while s <= n - m:
 