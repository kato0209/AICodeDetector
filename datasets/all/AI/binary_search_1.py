def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid  # 要素が見つかった場合、その位置（インデックス）を返す
        if guess > target:
            high = mid - 1  # 探索範囲を下半分に絞る
        else:
            low = mid + 1  # 探索範囲を上半分に絞る

    return None  # 要素が見つからなかった場合

# テストコード
if __name__ == '__main__':
    my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17]
    print(binary_search(my_list, 3))  # 出力: 1
    print(binary_search(my_list, -1)) # 出力: None
