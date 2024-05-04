def merge_sort_iterative(arr):
    width = 1
    n = <extra_id_0>   while <extra_id_1> n:
        for i in range(0, n, width * 2):
            left = i
  <extra_id_2>         mid = min(i + width, n)
            right = min(i + 2 <extra_id_3> n)

     <extra_id_4>      merged = []
    <extra_id_5>     <extra_id_6> l, r <extra_id_7> mid
  <extra_id_8>         while