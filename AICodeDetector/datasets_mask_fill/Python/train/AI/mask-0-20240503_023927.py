def binary_search(arr, target, low, high):
    if low > high:
     <extra_id_0>  return None

    mid = (low <extra_id_1> // 2
    if arr[mid] == <extra_id_2>       return mid
    elif arr[mid] < target:
        return binary_search(arr, <extra_id_3> + <extra_id_4>    else:
       <extra_id_5> binary_search(arr, target, low, mid - 1)

def exponential_search(arr, target):
    if len(arr) == 0:
        return None

   <extra_id_6> 指数的に増加しながら探索範囲を特定
   <extra_id_7> = 1
   <extra_id_8> bound < len(arr) and arr[bound] < target:
  