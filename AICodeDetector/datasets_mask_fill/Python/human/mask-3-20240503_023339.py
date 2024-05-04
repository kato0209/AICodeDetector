import sys
input = sys.stdin.readline

n, m = [int(x) for x in <extra_id_0> nは頂点の数、mは辺の数
g = <extra_id_1> _ in range(n)] # <extra_id_2> in range(m):
  <extra_id_3> a, b = <extra_id_4> x in input().split()]
    g[a].append(b)
  <extra_id_5> g[b].append(a)

from collections import <extra_id_6>    queue = deque([u])
    d = [None] * n # uからの距離の初期化
    d[u] = 0 # 自分との距離は0
 <extra_id_7>  while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i] is None:
           <extra_id_8>    d[i]