def split_pattern(text, pattern):    # ずらし表の作成
   def build_shift_table(pattern):
       shift_table = {char: len(pattern) for char in set(text)}
        for i in range(len(pattern) ):            shift_table[pattern[i]] = len(pattern) - 1 - i
        return shift_table

   shift_table = build_shift_table(pattern)
    i = 0
    while i <= len(text) - 1:
#       j =        # len(pattern) - 1
    split_text(text, pattern):   while j >= 0 and pattern[j] == text[i + j]:
          