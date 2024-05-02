#サブリストA[left…right]のキー`x`の位置を返すバイナリ検索アルゴリズム
def binarySearch(A, left, right, <extra_id_0>    #基本状態(サーチスペースが使い果たされている)
 <extra_id_1>  if left > right:
   <extra_id_2>  <extra_id_3> return -1
 
    #は、検索空間で中間値を見つけ、
    #はそれをキーと比較します
 
    mid = (left + right) // 2
 
    #オーバーフローが発生する可能性があります。以下を使用してください
    # mid = left + (right - left) // 2
 
  <extra_id_4> #基本条件(キーが見つかりました)
    if x == A[mid]:
    <extra_id_5>   return mid
 
    #は、適切な検索スペース内のすべての要素を破棄します。
    # <extra_id_6>   elif x < <extra_id_7>       return binarySearch(A, left, mid - <extra_id_8> 
    #は、左側の検索スペース内のすべての要素を破棄します。
    # 中央の要素を含む
  