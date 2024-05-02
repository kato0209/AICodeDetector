def linear_search(arr, target):
   <extra_id_0> i in range(len(arr)):
   <extra_id_1>    if <extra_id_2> target:
            return i  # 目的の要素が見つかった場合、そのインデックスを返す
    return None  # 要素が見つからなかった場合

# テストコード
if __name__ == '__main__':
 <extra_id_3>  my_list = [1, <extra_id_4> 7, <extra_id_5> 13, 15, 17]
    print(linear_search(my_list, 11))  # 出力: 5
    print(linear_search(my_list, -1)) # 出力: None
