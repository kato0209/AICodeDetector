# 深さ優先探索（帰りがけ）
import sys
input = sys.stdin.readline
from collections import deque

# グラフの作成(無向グラフでは#を消す)
N = int(input())
graph = [deque([]) for _ in range(N + 1)]
for _ in range(N):
    u, k, * v = [int(x) for x in input().split()] # uは頂点番号、kは隣接頂点の個数
    v.sort()
    for i in v:
        graph[u].append(i)
        # graph[i].append(u) # 無向グラフ

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
        if graph[v]:
            w = graph[v].popleft()
            if arrive[w] < 0:
                arrive[w] = 1
                stack.append(w) 
        else:
            time += 1
            finish_time[v] = time
            stack.pop()          
    return finish_time

# 孤立している頂点対策
for i in range(N):
    if arrive[i + 1] < 0:
        ans = dfs(i + 1)

# 頂点番号、終了時刻
for j in range(N):
    temp = [j + 1, ans[j + 1]]
    print(* temp)
