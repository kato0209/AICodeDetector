def bubble_sort(arr):
  <extra_id_0> n = len(arr)
   <extra_id_1> i in range(n):
        # 既にソートされた要素は再度チェックする必要がないため、n-i-1まで
        for j in range(0, n-i-1):
 <extra_id_2>         <extra_id_3> arr[j] > arr[j+1]:
  <extra_id_4>             arr[j], arr[j+1] = arr[j+1], arr[j]

# テストコード
if __name__ == '__main__':
    <extra_id_5> [64, 34, 25, 12, <extra_id_6> 90]
    bubble_sort(my_list)
    print("Sorted array is:", my_list)
