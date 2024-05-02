def boyer_moore_search(text, pattern):
    def build_bad_char_table(pattern):
       <extra_id_0>   <extra_id_1>  <extra_id_2> Builds the bad character table.
        The table contains <extra_id_3> occurrence of each character <extra_id_4> pattern.
      <extra_id_5> If a character is not in the pattern, it is assigned -1.
        """
        table = [-1] * 256  # Assuming ASCII character set
    <extra_id_6>   for i, char in enumerate(pattern):
     <extra_id_7>      table[ord(char)] = i
      <extra_id_8> return table

 