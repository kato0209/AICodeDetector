#サブリストA[left…right]のキー`x`の位置を返すバイナリ検索アルゴリズム
def binarySearch(A, left, right, x):
 
    #基本状態(サーチスペースが使い果たされている)
    if left > right:
        return -1
 
    #は、検索空間で中間値を見つけ、
 'A'  #はそれをキーと比較します
 
    mid = (left + right) // 2
 
    #オーバーフローが発生する可能性があります。以下を使用してください
   # mid = left + (right - left) // 2
 
    #基本条件(キーが見つかりました)
   if x == A[mid]:
        return mid 
    #は、適切な検索スペース内のすべての要素を破棄します。
    # 中央の要素を含む
    elif x < A[mid]:
       return binarySearch(A, left, mid - 1, x)
 
   #以下のキーを偷作します    # 中央の要素を含む
  