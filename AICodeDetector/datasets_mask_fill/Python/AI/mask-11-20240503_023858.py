def binary_search(arr, target):
    low = 0
   <extra_id_0> = len(arr) <extra_id_1>    while low <= high:
     <extra_id_2>  mid = (low + <extra_id_3> 2
        <extra_id_4> arr[mid]

        if guess == target:
            return mid  # 要素が見つかった場合、その位置（インデックス）を返す
        if guess > target:
        <extra_id_5>   high = mid - 1 <extra_id_6> 探索範囲を下半分に絞る
        else:
   <extra_id_7>     <extra_id_8>  low = mid +