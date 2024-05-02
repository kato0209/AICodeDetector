#サブリストA[left…right]のキー`x`の位置を返すバイナリ検索アルゴリズム
def binarySearch(A, left, right, x):
 
    #基本状態(サーチスペースが使い果たされている)
    if left > right:
        return -1
 
    #は、検索空間で中間値を見つけ、
    #はそれをキーと比較します
 
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
 
    #は、左側の検索スペース内のすべての要素を破棄します。
    # 中央の要素を含む
    else:
        return binarySearch(A, mid + 1, right, x)
 
 
#長さ`n`の指定されたリスト`A`内のキー`x`の位置を返します
def exponentialSearch(A, x):
 
    #ベースケース
    if not A:
        return -1
 
    bound = 1
 
    #は、キー`x`が存在する範囲を検索します
    while bound < len(A) and A[bound] < x:
        bound *= 2        #は2の次の累乗を計算します
 
    #はA[bound/2 … min(bound, n-1)]でバイナリ検索を呼び出します
    return binarySearch(A, bound // 2, min(bound, len(A) - 1), x)
 
 
#指数検索アルゴリズム
if __name__ == '__main__':
 
    A = [2, 5, 6, 8, 9, 10]
    key = 9
 
    index = exponentialSearch(A, key)
 
    if index != -1:
        print('Element found at index', index)
    else:
        print('Element found not in the list')