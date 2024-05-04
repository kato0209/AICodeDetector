def boyer_moore_search(text, pattern):
 <extra_id_0>  def build_bad_char_table(pattern):
        """
     <extra_id_1>  Builds the bad character table.
       <extra_id_2> table contains the rightmost occurrence of each character in the pattern.
       <extra_id_3> a character is not in the pattern, it is <extra_id_4>        """
     <extra_id_5>  table = [-1] * 256  # Assuming ASCII character set
    <extra_id_6>   <extra_id_7> char in enumerate(pattern):
            table[ord(char)] = i
 <extra_id_8>      return table

 