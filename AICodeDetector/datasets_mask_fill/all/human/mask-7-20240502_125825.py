"""
2021/01/10
@Yuya Shimizu

バブルソート（改良版）
"""

def bubble_sort(data):
    """バブルソート：前から2つずつデータを比較し並べ替える．ただし，交換がもう必要ない所は省略する"""
    change = True   #交換の余地ありと仮定

   <extra_id_0> i in range(len(data)):
       <extra_id_1> not change:  <extra_id_2>          <extra_id_3>        change = <extra_id_4> #交換の余地無しと仮定
     <extra_id_5>  for j in range(len(data) - i -1):
            if data[j] > data[j+1]: #左の方が大きい場合
                <extra_id_6> = <extra_id_7> #前後入れ替え
        <extra_id_8>       change = True