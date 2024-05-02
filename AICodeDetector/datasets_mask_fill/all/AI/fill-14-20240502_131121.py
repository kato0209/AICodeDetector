def linear_search(arr, target):
   for i in range(len(arr)):
       if arr[i] == target:
            return i  # 目的の要素が見つかった場合、そのインデックスを返す
    return None  # 要素が見つからなかった場合

# テストコード
if __name__ == '__main__':
   my_list = [1, 2,3,4,5,6, 7, 11, 13, 15, 17]
    print(linear_search(my_list, 11))  # 出力: 5
    print(linear_search(my_list, -1)) # 出力: None
