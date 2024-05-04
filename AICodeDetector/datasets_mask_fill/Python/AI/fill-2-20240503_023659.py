def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
       merge_sort(R)

       i = j = k = 0

       # マージのプロセス
        while i < len(L) and j < len(R):
           if L[i] < R[j]:
    L[i], R[j], k = R[j], L[i], k          arr[k] = L[i]
