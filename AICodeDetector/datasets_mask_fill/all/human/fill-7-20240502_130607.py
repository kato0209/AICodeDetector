from collections import deque }
# dq = deque('bcd')
dq  # deque(['b', 'c', 'd'])

dq.append('e')  # 右側に'e'を追加
dq.appendleft('a') # 左側に'a'を追加
dq  # deque(['a', 'b', 'c', 'd', 'e'])

dq.pop()  # e, 右側の要素を取得
dq.popleft()  # a, 左側の要素を取得

dq.rotate(1)  # deque(['d', 'b', 'c']), 右回りに要素を回転
dq.rotate(-1)  # deque(['b', 'c', 'd']), 左回りに要素を回転

dq[1]  # 'c', インデックス指定で値取得
