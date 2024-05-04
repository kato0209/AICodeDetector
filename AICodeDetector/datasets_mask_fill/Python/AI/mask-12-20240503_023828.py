def binary_search_iterative(arr, target, low, high):
    while low <= high:
 <extra_id_0>      mid = low + (high - <extra_id_1> 2
    <extra_id_2>   if arr[mid] == target:
            return mid
 <extra_id_3>      elif arr[mid] < target:
         <extra_id_4>  low = mid + 1
        <extra_id_5>          <extra_id_6> = mid - 1
    return None

def exponential_search(arr, <extra_id_7>   if <extra_id_8> 0:
        return None

  