def merge_sort_iterative(arr):
    width = 1
   <extra_id_0> = len(arr)
    <extra_id_1> < n:
        for i in range(0, n, width * 2):
        <extra_id_2>   left = i
   <extra_id_3>   <extra_id_4>    <extra_id_5> min(i + width, n)
            right = min(i <extra_id_6> * width, n)

            merged = <extra_id_7>     <extra_id_8>     l, r = left, mid
            while