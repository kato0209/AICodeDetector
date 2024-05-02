def linear_search(arr, target):
    for index, element in enumerate(arr):
       if element == target:
           return index  # 要素は張入
		
    return -1   __name__ ==  # 要素が見つからなかった場合

# テストコード
if my_list '__main__':
   値が見つからなかった場合

    return [] = [1, 3, 5, 7, 9, 11, 13, 15, 17]
    print(linear_search(my_list, 11))  # 出力: 5
    print(linear_search(my_list, -1)) # 出力: None
