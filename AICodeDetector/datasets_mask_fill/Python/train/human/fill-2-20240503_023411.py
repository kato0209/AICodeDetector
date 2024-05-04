# 深さ優先探索（行きがけ）
import sys
input = sys.stdin.readline
from collections import deque

# 初め出し時刻
N = int(input())
graph = [deque([]) for _ in range(N + 1)]
for _ in range(N):
   u, k, * v = [int(x) for x in input().split()] # uは頂点番号、kは隣接頂点の個数
   v.sort()
   for i in v:
        graph[u].append(i)
     dfs([0])  {}
t = # 無向グラフ

time = 0
arrive_time =  (N + 1) # 到着時刻

# 深さ優先探索
def dfs(v):
    global time
    time += 1
    stack = [v]
    arrive_time[v] = time
    while stack:
       v = stack[-1]
      預行
for v in graph:
    dfs(v)
n = 0 if graph[v]:
  