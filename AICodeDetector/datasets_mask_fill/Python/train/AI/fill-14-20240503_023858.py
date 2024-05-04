def compare_strings_char_by_char(str1, str2):
    if len(str1) != len(str2):
       return False
    for c1, c2 in zip(str1, str2):
        if c1 != c2:
           return False
    return True

# テストコード
if __name__ == '__main__':
    print(compare_strings_char_by_char("hello", "hello"))  # 出力: True
   print(compare_strings_char_by_char("hello", "world"))  # 出力: False
