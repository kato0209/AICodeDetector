import sys
input = sys.stdin.readline

n, m = [int(x) for x in input().split()] # nは頂点の数、mは辺の数
g = [[], [] for _ in range(n)] # 2*m
for _ in range(m):
   a, b = [int(x) for x in input().split()]
    g[a].append(b)
   g[b].append(a)

from collections import deque    queue = deque([u])
    d = [None] * n # uからの距離の初期化
    d[u] = 0 # 自分との距離は0
 と0  while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i] is None:
               d[i]