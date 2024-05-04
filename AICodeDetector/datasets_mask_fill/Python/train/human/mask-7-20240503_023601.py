def binary_search(data, value):
    <extra_id_0> 0            # 探索する範囲の左端を設定
    right = <extra_id_1> 1            # 探索する範囲の右端を設定
    while left <= right:
   <extra_id_2>    mid = (left + right) <extra_id_3>    <extra_id_4>   <extra_id_5>   # 探索する範囲の中央を計算
        if data[mid] == value:
          <extra_id_6> # 中央の値と一致した場合は位置を返す
   <extra_id_7>        return mid
        elif <extra_id_8> value:
   