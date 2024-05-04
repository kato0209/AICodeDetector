def boyer_moore_search(text, <extra_id_0>   # 不良文字ヒューリスティックテーブルを作成
    def bad_character_heuristic(pattern):
 <extra_id_1>      bad_char = {}
 <extra_id_2>      length = len(pattern)
 <extra_id_3>      for i <extra_id_4>            # パターン内の各文字に対して、右端からの位置を記録
            bad_char[pattern[i]] = <extra_id_5> - i - 1)
        return bad_char

    # テキストとパターンの長さ
    n, m = len(text), len(pattern)

    # 不良文字ヒューリスティックテーブルを作成
  <extra_id_6> bad_char = bad_character_heuristic(pattern)

    s = <extra_id_7> # sはテキスト内のパターンの開始位置を指す
    while s <= <extra_id_8> m:
 