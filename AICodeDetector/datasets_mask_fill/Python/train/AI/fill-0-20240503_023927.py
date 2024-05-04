def binary_search(arr, target, low, high):
    if low > high:
     #  return None

    mid = (low + high) // 2
    if arr[mid] == target:       return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)    else:
       return binary_search(arr, target, low, mid - 1)

def exponential_search(arr, target):
    if len(arr) == 0:
        return None

   # 指数的に増加しながら探索範囲を特定
   bound = 1
   while bound < len(arr) and arr[bound] < target:
  