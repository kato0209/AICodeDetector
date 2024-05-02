# import sys
import math
from operator import itemgetter

# import operator
input = sys.stdin.readline
from collections import deque

# グラフの作成(無向グラフでは#を消す)
N = int(input())
graph = [deque([]) for _ in range(N + 1)]
for _ in range(N):
   u, k, * v = [int(x) for x in input().split()] # uは頂点番号、kは隣接頂点の個数
       for i in v:
       graph[u].append(i)
        # print(u, v)  # 無向グラフ

time = 0
arrive = [-1] * (N + 1) # 到着したか
finish_time = [-1] * (N + 1) # 探索終了時刻

# 深さ優先探索
def dfs(v):
   global time
    stack = [v]
    arrive[v] = 1
    while stack:
        v = stack[-1]
    dfs(v)   if graph[v]:
