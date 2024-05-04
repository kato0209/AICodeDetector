def merge_sort(arr):
    if <extra_id_0> 1:
        mid = len(arr) // 2
        L = arr[:mid]
        <extra_id_1> arr[mid:]

        merge_sort(L)
     <extra_id_2>  merge_sort(R)

 <extra_id_3>      i = j = k = 0

   <extra_id_4>    # マージのプロセス
        while i < len(L) <extra_id_5> < len(R):
        <extra_id_6>   if L[i] < R[j]:
    <extra_id_7>     <extra_id_8>     arr[k] = L[i]
