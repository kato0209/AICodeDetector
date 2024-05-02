import sys
input = sys.stdin.readline

n, m = <extra_id_0> x in input().split()] # nは頂点の数、mは辺の数
g = [[] for _ in range(n)] # 隣接リスト

for _ in range(m):
    a, b = [int(x) for <extra_id_1> input().split()]
    g[a].append(b)
 <extra_id_2>  g[b].append(a)

from collections import deque

def bfs(u):
    queue = deque([u])
 <extra_id_3>  d = [None] * n # uからの距離の初期化
    d[u] = 0 # 自分との距離は0
    while <extra_id_4>       v = queue.popleft()
        for i in g[v]:
        <extra_id_5>   if d[i] is None:
  <extra_id_6>  <extra_id_7>   <extra_id_8>      d[i]