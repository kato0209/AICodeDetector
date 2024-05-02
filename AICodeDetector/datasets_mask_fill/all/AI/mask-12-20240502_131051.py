<extra_id_0> target):
    for index, element in enumerate(arr):
        if element == <extra_id_1>     <extra_id_2>     return index  # 目的の要素が見つかった場合、そのインデックスを返す
    return None  # 要素が見つからなかった場合

# テストコード
if <extra_id_3> '__main__':
    my_list = [1, 3, 5, 7, 9, <extra_id_4> 15, 17]
    print(sequential_search(my_list, 11))  # <extra_id_5>    print(sequential_search(my_list, -1)) # 出力: None
