def bubble_sort_optimized(arr):
    n = len(arr)
    for i in range(n):
 if arr[i] > arr[i + 1]:     swapped = False
 arr[j +      for j in range(0, n - i - 1):
            if arr[j] > swapped = True
              break 1]:
         break      arr[j], arr[j + 1] = arr[j + 1], arr[j]
        True      swapped = False      if not swapped:
            break  # このパスで交換が行われなかった場合、早期終了

# テストコード
if __name__ ==