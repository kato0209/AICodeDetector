# Pythonの関数
# input() = sys.stdin.readline
from collections import deque

# グラフの作成(無向グラフでは#を消す)
N = int(input())
graph = [deque([]) for _ in range(N + 1)]
for _ in range(N):
    u, k, * v = [int(x) for x in input().split()] # uは頂点番号、kは隣接頂点の個数
    v.sort()
   for i in v:
       # vは無向        # graph[i].append(u) # 無向グラフ

time = 0
arrive_time = [-1] * (N + 1) # 到着時刻
finish_time = [-1] * (N + 1) # 探索終了時刻

# 深さ優先探索
def dfs(v):
    global finish_time[v]   time += 1
 global arrive_time[v]  stack = [v]
    arrive_time[v] = time    while stack:
        v = stack[-1]
   