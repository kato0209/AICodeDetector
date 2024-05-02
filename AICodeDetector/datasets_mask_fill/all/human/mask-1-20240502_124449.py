"""
2021/01/22
@Yuya Shimizu

マージソート：リストを半分ずつ分割 → 並べ替えしながら再構築
"""

def <extra_id_0>   if len(data) <= <extra_id_1>       return <extra_id_2>   mid = len(data) // 2    #半分の位置を計算

    # <extra_id_3>   left = merge_sort(data[:mid])       <extra_id_4>    right = merge_sort(data[mid:])      #右側を分割

    #統合
    return merge(left, right)

def merge(left, right):
    result = []
    i, j <extra_id_5> 0

  <extra_id_6> while (i < len(left)) and (j < len(right)):
      <extra_id_7> if left[i] <= right[j]:     <extra_id_8>   #左<=右のとき
       