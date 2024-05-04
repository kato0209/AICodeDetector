def <extra_id_0>    # ずらし表の作成
 <extra_id_1>  def build_shift_table(pattern):
 <extra_id_2>      <extra_id_3> {char: len(pattern) for char in set(text)}
        for i in range(len(pattern) <extra_id_4>            shift_table[pattern[i]] = len(pattern) - 1 - i
        return shift_table

 <extra_id_5>  shift_table = build_shift_table(pattern)
    i = 0
    while i <= len(text) <extra_id_6>        <extra_id_7> len(pattern) - 1
    <extra_id_8>   while j >= 0 and pattern[j] == text[i + j]:
          