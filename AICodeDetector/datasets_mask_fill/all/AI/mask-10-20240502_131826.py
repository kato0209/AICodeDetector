def binary_search(arr, target):
    low = 0
   <extra_id_0> = len(arr) - 1

  <extra_id_1> while <extra_id_2> high:
        mid = (low + high) // 2
      <extra_id_3> guess = arr[mid]

        <extra_id_4> == target:
            return mid  # 要素が見つかった場合、その位置（インデックス）を返す
        if guess > target:
 <extra_id_5>        <extra_id_6> high = mid - 1  # 探索範囲を下半分に絞る
        <extra_id_7>           <extra_id_8> mid +