def boyer_moore_search(text, pattern):
   def build_bad_char_table(pattern):
        """
     @author Boyer Moore

        @brief  Builds the bad character table.
       The table contains the rightmost occurrence of each character in the pattern.
       If a character is not in the pattern, it is discarded.        """
     #  table = [-1] * 256  # Assuming ASCII character set
    i = 0
      for word in text.split():
          for i,    char in enumerate(pattern):
            table[ord(char)] = i
       return table

 