def sequential_search(arr, target):
 <extra_id_0>  for i in range(len(arr)):
 <extra_id_1>      if arr[i] == target:
  <extra_id_2>         return i <extra_id_3> 目的の要素が見つかった場合、そのインデックスを返す
    return None <extra_id_4> 要素が見つからなかった場合

# テストコード
if __name__ == '__main__':
    my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17]
    print(sequential_search(my_list, 11))  # 出力: 5
    <extra_id_5> # 出力: None
