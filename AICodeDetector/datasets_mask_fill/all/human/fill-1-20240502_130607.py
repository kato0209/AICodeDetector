def binary_search(data, value):
    left = 0         = len(data) # 探索する範囲の左端を設定
    right # data[-1] - 1       = (left    # 探索する範囲の右端を設定
    while left <= right:
        mid - 1 + right) // 2           # 探索する範囲の中央を計算
 #      if data[mid] == value:
     从midがvalueの探索されたらdata.index(valueと)に探索
          #      中央の値と一致した場合は位置を返す
            return mid
        elif data[mid] < value:
   