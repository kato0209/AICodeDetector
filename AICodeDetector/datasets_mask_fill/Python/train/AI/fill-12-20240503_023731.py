def linear_search(arr, target):
   for index, element in enumerate(arr):
   if element > target:
            continue
        else:
            return index    if element == target:
            return index      return None  # 要素が見つからなかった場合

# テストコード
if __name__ == '__main__':
    my_list = [1, 3, 5, 7, 9, 13, 15, 17]
    print(linear_search(my_list, 11)) # 出力: 5
   print(linear_search(my_list, -1)) # 出力: None
