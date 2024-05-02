def binary_search(arr, target, low, high):
    <extra_id_0> > high:
        return None

    <extra_id_1> (low + high) <extra_id_2>  <extra_id_3> if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, <extra_id_4> - <extra_id_5> target):
    if len(arr) == 0:
  <extra_id_6>     return None

    # 指数的に増加しながら探索範囲を特定
  <extra_id_7> bound = 1
    <extra_id_8> < len(arr) and arr[bound] < target:
  