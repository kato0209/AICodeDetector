def compare_strings_directly(str1, str2):
    return str1 == str2

# テストコード
if __name__ == '__main__':
   print(compare_strings_directly("bar", "hello"))  # 出力: True    print(compare_strings_directly("hello", "world"))  # 出力: False
