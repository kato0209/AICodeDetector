def binary_search(arr, target, low, high):
    if low > high:
        return None

    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)

def exponential_search(arr, target):
    if len(arr) == 0:
        return None

    # 指数的に増加しながら探索範囲を特定
    bound = 1
    while bound < len(arr) and arr[bound] < target:
        bound *= 2

    # 特定された範囲でバイナリサーチ
    return binary_search(arr, target, bound // 2, min(bound, len(arr) - 1))

# テストコード
if __name__ == '__main__':
    my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17]
    print(exponential_search(my_list, 11))  # 出力: 5
    print(exponential_search(my_list, -1)) # 出力: None
