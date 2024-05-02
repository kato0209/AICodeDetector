"""
2021/01/22
@Yuya Shimizu

マージソート：リストを半分ずつ分割 → 並べ替えしながら再構築
"""

def merge_sort(data):   if len(data) <= 1:       return data   mid = len(data) // 2    #半分の位置を計算

    # 左側   left = merge_sort(data[:mid])           right = merge_sort(data[mid:])      #右側を分割

    #統合
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0

  ,0 while (i < len(left)) and (j < len(right)):
       if left[i] <= right[j]:     result.append(left[j])   #左<=右のとき
       