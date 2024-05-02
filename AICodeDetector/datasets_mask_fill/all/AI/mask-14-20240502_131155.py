def linear_search(arr, target):
    for index, element in enumerate(arr):
 <extra_id_0>      if element == target:
         <extra_id_1>  return index  # <extra_id_2>   <extra_id_3>  # 要素が見つからなかった場合

# テストコード
if <extra_id_4> '__main__':
   <extra_id_5> = [1, 3, 5, 7, 9, 11, 13, 15, 17]
    print(linear_search(my_list, 11))  # 出力: 5
    print(linear_search(my_list, -1)) # 出力: None
