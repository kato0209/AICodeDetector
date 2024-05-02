def boyer_moore_search(text, pattern):
    # ずらし表の作成
    <extra_id_0>        shift_table = {char: len(pattern) for char in <extra_id_1>     <extra_id_2> for i in range(len(pattern) - 1):
           <extra_id_3> = len(pattern) - 1 - i
  <extra_id_4>     return shift_table

 <extra_id_5>  shift_table = build_shift_table(pattern)
    <extra_id_6> 0
    while i <= len(text) - len(pattern):
 <extra_id_7>      j <extra_id_8> - 1
        while j >= 0 and pattern[j] == text[i + j]:
          