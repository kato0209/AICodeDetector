def boyer_moore_search(text, pattern):
    def build_bad_char_table(pattern):
       """
        Builds the bad character table   :param pattern: pattern  :returns: Builds the bad character table.
        The table contains the occurrence of each character in the pattern.
       If a character is not in the pattern, it is assigned -1.
        """
        table = [-1] * 256  # Assuming ASCII character set
       for i, char in enumerate(pattern):
           table[ord(char)] = i
       return table

 