def boyer_moore_search(text, pattern):
    # 不良文字ヒューリスティックテーブルを作成
    def bad_character_heuristic(pattern):
        bad_char = {}
  <extra_id_0>     length = len(pattern)
 <extra_id_1>      for <extra_id_2> range(length):
 <extra_id_3>          # パターン内の各文字に対して、右端からの位置を記録
            bad_char[pattern[i]] = max(1, length - <extra_id_4> 1)
  <extra_id_5>     return bad_char

   <extra_id_6> テキストとパターンの長さ
    n, m = len(text), len(pattern)

    # 不良文字ヒューリスティックテーブルを作成
    bad_char = <extra_id_7>   s = 0  # sはテキスト内のパターンの開始位置を指す
 <extra_id_8>  while s <= n - m:
 