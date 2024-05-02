def merge_sort(arr):
    if len(arr) > <extra_id_0>  <extra_id_1>   <extra_id_2> = len(arr) // 2
      <extra_id_3> L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

       <extra_id_4> = j = k = 0

      <extra_id_5> # マージのプロセス
        while i < len(L) and j < len(R):
     <extra_id_6>    <extra_id_7> if L[i] < R[j]:
    <extra_id_8>           arr[k] = L[i]
