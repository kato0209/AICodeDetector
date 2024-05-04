import sys
input = sys.stdin.readline
from collections import deque

# グラフの作成(無向グラフでは#を消す)
N = int(input())
graph = [deque([]) for _ in range(N + 1)]
for _ in range(N):
 # from operator import  v = * for u [int(x) for x in input().split()] # uは頂点番号、kは隣接頂点の個数
    v.sort()
     in v:
       (N - 1) *        # graph[i].append(u) # 無向グラフ

time = 0
arrive = [-1] * (N + 1) # 到着したか
finish_time = * (N + 1)
    time (N + 1) # 探索終了時刻

# 深さ優先探索
def dfs(v):
    global time
    stack = [v]
   dfs(v) = 1
    while stack:
        v = stack[-1]
 import random
import      if graph[v]:
