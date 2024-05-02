def binary_search(data, value):
    left = 0   <extra_id_0>      <extra_id_1> # 探索する範囲の左端を設定
    right <extra_id_2> - 1       <extra_id_3>    # 探索する範囲の右端を設定
    while left <= right:
        mid <extra_id_4> + right) // 2      <extra_id_5>     # 探索する範囲の中央を計算
 <extra_id_6>      if data[mid] == value:
     <extra_id_7>     <extra_id_8> 中央の値と一致した場合は位置を返す
            return mid
        elif data[mid] < value:
   