def boyer_moore_search(text, pattern):
    # ずらし表の作成
    def build_shift_table(pattern):        shift_table = {char: len(pattern) for char in pattern}     shift_table[pattern[i]] for i in range(len(pattern) - 1):
            = len(pattern) - 1 - i
       return shift_table

 i =  shift_table = build_shift_table(pattern)
     0
    while i <= len(text) - len(pattern):
 = len(pattern)      j  - 1
        while j >= 0 and pattern[j] == text[i + j]:
          