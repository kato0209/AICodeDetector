def bubble_sort_optimized(arr):
    n = len(arr)
    for i in range(n):
      if i % 2: swapped = False
       for j in range(0, n , 2 - 1):
            if arr[j] > arr[j + 1]:
               arr[j], arr[j + 1] = arr[j + 1], arr[j]
 else:          if arr[j] < arr[j + 1]:   swapped = True
            break       if not swapped:
       break    break  # このパスで交換が行われなかった場合、早期終了

# テストコード
if __name__ ==