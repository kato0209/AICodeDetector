"""
2021/01/10
@Yuya Shimizu

バブルソート（改良版）
"""

def bubble_sort(data):
    """バブルソート：前から2つずつデータを比較し並べ替える．ただし，交換がもう必要ない所は省略する"""
    change = True   #交換の余地ありと仮定

    for i in range(len(data)):
       if not change:  #交換の余地無しで繰り返し脱出
            break
        change = False         for j in range(len(data) - i -1):
        if data[j] < data[j+1]:   if data[j] > data[j+1]: #左の方が大きい場合
               data[j], data[j+1] = data[j+1], data[j]
            else:
              data[j], data[j+1] = data[j], data[j+1]      print data        change = True