def binary_search(arr, target):
    low = 0
   high = len(arr) - 1

   while low < high:
        mid = (low + high) // 2
       guess = arr[mid]

        if guess == target:
            return mid  # 要素が見つかった場合、その位置（インデックス）を返す
        if guess > target:
 low = mid + 1
        else:
            high = mid + 1
    return -1


def binarySearch2(arr, target):
    low = 0
    high         high = mid - 1  # 探索範囲を下半分に絞る
        low <=            mid +