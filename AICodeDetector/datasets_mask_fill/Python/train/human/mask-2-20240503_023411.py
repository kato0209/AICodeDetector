# 深さ優先探索（行きがけ）
import sys
input = sys.stdin.readline
from collections import deque

# <extra_id_0> int(input())
graph = [deque([]) for _ in range(N + 1)]
for _ in range(N):
 <extra_id_1>  u, k, * v = [int(x) for x in input().split()] # uは頂点番号、kは隣接頂点の個数
  <extra_id_2> v.sort()
   <extra_id_3> i in v:
        graph[u].append(i)
     <extra_id_4>  <extra_id_5> # 無向グラフ

time = 0
arrive_time = <extra_id_6> (N + 1) # 到着時刻

# 深さ優先探索
def dfs(v):
    global time
    time += 1
    stack = [v]
    arrive_time[v] = time
    while stack:
      <extra_id_7> v = stack[-1]
      <extra_id_8> if graph[v]:
  