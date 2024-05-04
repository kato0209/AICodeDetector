def merge_sort_iterative(arr):
    width = 1
    n = len(arr)
    while width < n:
        for i in range(0, n, width * 2):
            left = i
            mid = min(i + width, n)
            right = min(i + 2 * width, n)

            merged = []
            l, r = left, mid
            while l < mid and r < right:
                if arr[l] < arr[r]:
                    merged.append(arr[l])
                    l += 1
                else:
                    merged.append(arr[r])
                    r += 1
            merged.extend(arr[l:mid])
            merged.extend(arr[r:right])
            arr[left:right] = merged

        width *= 2

# テストコード
if __name__ == '__main__':
    my_list = [12, 11, 13, 5, 6, 7]
    merge_sort_iterative(my_list)
    print("Sorted array is:", my_list)
