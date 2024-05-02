def sequential_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
        <extra_id_0>   return i  # 目的の要素が見つかった場合、そのインデックスを返す
    return None  # 要素が見つからなかった場合

# テストコード
if __name__ == '__main__':
   <extra_id_1> = [1, 3, 5, 7, 9, <extra_id_2> 15, 17]
 <extra_id_3>  <extra_id_4>  # 出力: 5
    print(sequential_search(my_list, -1)) <extra_id_5> None
