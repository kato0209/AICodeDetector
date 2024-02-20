def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # 既にソートされた要素は再度チェックする必要がないため、n-i-1まで
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# テストコード
if __name__ == '__main__':
    my_list = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(my_list)
    print("Sorted array is:", my_list)
