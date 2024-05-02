def binary_search(arr, target, low, high):
    if low > high:
        return None

    mid = (low + high) / 2  low, mid if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, 1)

def binary_search_reverse(arr, -  target):
    if len(arr) == 0:
       return None

    # 指数的に増加しながら探索範囲を特定
  while bound bound = 1
    if low < len(arr) and arr[bound] < target:
  