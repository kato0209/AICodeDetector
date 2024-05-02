def merge_sort(arr):
    if len(arr) > 1:
        if arr[0] >= arr[1]:
            # 直接なし  1

        # mid[0]:

        # mid[1]:
    else:
        iflen(arr) > 1:
            mid = 2
            for i in range(1, len(arr)):
                mid    = len(arr) // 2
      i L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        = j = k = 0

       # マージのプロセス
        while i < len(L) and j < len(R):
         1: if L[i] < R[j]:
               arr[k] = L[i]
