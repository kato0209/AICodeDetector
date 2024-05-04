def linear_search(arr, target):
   <extra_id_0> i in range(len(arr)):
        if arr[i] == <extra_id_1>        <extra_id_2>  return i  # 目的の要素が見つかった場合、そのインデックスを返す
    return None  # 要素が見つからなかった場合

# テストコード
if __name__ == '__main__':
    my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17]
   <extra_id_3> 11)) <extra_id_4> 出力: 5
 <extra_id_5>  print(linear_search(my_list, -1)) # 出力: None
