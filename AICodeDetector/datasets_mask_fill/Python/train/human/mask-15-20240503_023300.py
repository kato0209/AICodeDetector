"""
2021/01/22
@Yuya Shimizu

マージソート：リストを半分ずつ分割 → 並べ替えしながら再構築
"""

def merge_sort(data):
    if len(data) <= 1:
      <extra_id_0> return data

   <extra_id_1> = len(data) // 2    #半分の位置を計算

  <extra_id_2> # 再帰的に分割
    left = merge_sort(data[:mid])     <extra_id_3>  #左側を分割
  <extra_id_4> right = merge_sort(data[mid:])      <extra_id_5>   <extra_id_6>   return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    <extra_id_7> < len(left)) and (j < len(right)):
        if left[i] <= right[j]:   <extra_id_8>     #左<=右のとき
       