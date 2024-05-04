def linear_search(arr, target):
   <extra_id_0> index, element in enumerate(arr):
   <extra_id_1>    if element == target:
            return index  <extra_id_2>    return None  # 要素が見つからなかった場合

# テストコード
if __name__ == '__main__':
    my_list = [1, 3, 5, 7, <extra_id_3> 13, 15, 17]
    print(linear_search(my_list, 11)) <extra_id_4> 出力: 5
   <extra_id_5> -1)) # 出力: None
