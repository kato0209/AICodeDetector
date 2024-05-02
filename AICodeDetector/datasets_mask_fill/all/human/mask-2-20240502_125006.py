# 深さ優先探索（行きがけ）
import sys
input = <extra_id_0> import deque

# グラフの作成(無向グラフでは#を消す)
N = int(input())
graph = [deque([]) for _ in range(N + 1)]
for _ in range(N):
    u, k, * v = [int(x) for x in input().split()] # uは頂点番号、kは隣接頂点の個数
    <extra_id_1>   for i in v:
   <extra_id_2>  <extra_id_3> graph[u].append(i)
       <extra_id_4> graph[i].append(u) # 無向グラフ

time = 0
arrive_time = [-1] * (N + 1) # 到着時刻

# 深さ優先探索
def dfs(v):
    global time
    time += 1
  <extra_id_5> stack = [v]
   <extra_id_6> = <extra_id_7>   while stack:
       <extra_id_8> = stack[-1]
        if graph[v]:
  