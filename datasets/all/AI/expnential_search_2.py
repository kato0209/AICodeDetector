def binary_search_iterative(arr, target, low, high):
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None

def exponential_search(arr, target):
    if len(arr) == 0:
        return None

    # 指数的に増加しながら探索範囲を特定
    bound = 1
    while bound < len(arr) and arr[bound] < target:
        bound *= 2

    # 特定された範囲でバイナリサーチ（イテレーティブ）
    return binary_search_iterative(arr, target, bound // 2, min(bound, len(arr) - 1))

# テストコード
if __name__ == '__main__':
    my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17]
    print(exponential_search(my_list, 11))  # 出力: 5
    print(exponential_search(my_list, -1)) # 出力: None
