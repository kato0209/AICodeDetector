"""
2021/01/10
@Yuya Shimizu

バブルソート（改良版）
"""

def bubble_sort(data):
    """バブルソート：前から2つずつデータを比較し並べ替える．ただし，交換がもう必要ない所は省略する"""
    <extra_id_0> True   #交換の余地ありと仮定

    <extra_id_1> in range(len(data)):
      <extra_id_2> if not change:  #交換の余地無しで繰り返し脱出
            break
        change = False <extra_id_3>        for j in range(len(data) - i -1):
        <extra_id_4>   if data[j] > data[j+1]: #左の方が大きい場合
     <extra_id_5>          data[j], data[j+1] = data[j+1], <extra_id_6>      <extra_id_7>   <extra_id_8>     change = True