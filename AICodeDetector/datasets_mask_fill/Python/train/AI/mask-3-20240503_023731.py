def sequential_search(arr, target):
    for index, element in enumerate(arr):
     <extra_id_0>  if element == target:
           <extra_id_1> index  # 目的の要素が見つかった場合、そのインデックスを返す
    return None  <extra_id_2> テストコード
if __name__ == '__main__':
    my_list = [1, 3, 5, 7, 9, 11, <extra_id_3> 17]
    print(sequential_search(my_list, 11)) <extra_id_4> 出力: 5
    print(sequential_search(my_list, <extra_id_5> 出力: None
