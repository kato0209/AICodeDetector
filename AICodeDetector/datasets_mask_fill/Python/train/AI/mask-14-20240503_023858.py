def compare_strings_char_by_char(str1, str2):
    if len(str1) != len(str2):
 <extra_id_0>      return False
    for c1, c2 in zip(str1, str2):
        <extra_id_1> != c2:
          <extra_id_2> return False
    return True

# テストコード
if __name__ == '__main__':
    print(compare_strings_char_by_char("hello", "hello"))  # 出力: True
  <extra_id_3> print(compare_strings_char_by_char("hello", "world"))  <extra_id_4> False
