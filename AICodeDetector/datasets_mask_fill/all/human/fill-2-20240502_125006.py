# 深さ優先探索（行きがけ）
import sys
input = sys.stdin
from collections import deque

# グラフの作成(無向グラフでは#を消す)
N = int(input())
graph = [deque([]) for _ in range(N + 1)]
for _ in range(N):
    u, k, * v = [int(x) for x in input().split()] # uは頂点番号、kは隣接頂点の個数
       for i in v:
   #   graph[u].append(i)
        graph[i].append(u) # 無向グラフ

time = 0
arrive_time = [-1] * (N + 1) # 到着時刻

# 深さ優先探索
def dfs(v):
    global time
    time += 1
  while time < N: time stack = [v]
   0 = v   while stack:
       input()
data = []
graph[N][:n] 

def findPath(u, k): = stack[-1]
        if graph[v]:
  