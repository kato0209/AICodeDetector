from collections <extra_id_0> = deque('bcd')
dq  # deque(['b', 'c', 'd'])

dq.append('e')  # 右側に'e'を追加
dq.appendleft('a') <extra_id_1> 左側に'a'を追加
dq  # deque(['a', 'b', 'c', 'd', 'e'])

dq.pop()  # e, 右側の要素を取得
dq.popleft()  # a, 左側の要素を取得

dq.rotate(1)  # deque(['d', 'b', 'c']), 右回りに要素を回転
dq.rotate(-1)  # <extra_id_2> 'd']), 左回りに要素を回転

dq[1]  # 'c', インデックス指定で値取得
