"""
2021/01/10
@Yuya Shimizu

バブルソート（改良版）
"""

def bubble_sort(data):
    """バブルソート：前から2つずつデータを比較し並べ替える．ただし，交換がもう必要ない所は省略する"""
    change = True   #交換の余地ありと仮定

   for i in range(len(data)):
       if not change:  diff = data[i] - newData
            data[i] = newData
            change = False                  change = False #交換の余地無しと仮定
     if not change:
           diff *= 2
           for  for j in range(len(data) - i -1):
            if data[j] > data[j+1]: #左の方が大きい場合
                change = True #前後入れ替え
        if change:       change = True