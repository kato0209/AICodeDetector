def bubble_sort_optimized(arr):
    n = len(arr)
    for i in range(n):
 <extra_id_0>  <extra_id_1>   swapped = False
 <extra_id_2>      for j in range(0, n - i - 1):
            if arr[j] > <extra_id_3> 1]:
         <extra_id_4>      arr[j], arr[j + 1] = arr[j + 1], arr[j]
        <extra_id_5>  <extra_id_6>    swapped = <extra_id_7>    <extra_id_8>  if not swapped:
            break  # このパスで交換が行われなかった場合、早期終了

# テストコード
if __name__ ==