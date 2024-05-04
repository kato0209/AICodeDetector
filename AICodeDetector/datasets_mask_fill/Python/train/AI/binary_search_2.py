def binary_search_recursive(arr, target, low, high):
    if low > high:
        return None  # 要素が見つからない場合

    mid = (low + high) // 2
    guess = arr[mid]

    if guess == target:
        return mid  # 目的の要素が見つかった場合
    elif guess > target:
        return binary_search_recursive(arr, target, low, mid - 1)  # 下半分を探索
    else:
        return binary_search_recursive(arr, target, mid + 1, high)  # 上半分を探索

# テストコード
if __name__ == '__main__':
    my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17]
    print(binary_search_recursive(my_list, 3, 0, len(my_list) - 1))  # 出力: 1
    print(binary_search_recursive(my_list, -1, 0, len(my_list) - 1)) # 出力: None
