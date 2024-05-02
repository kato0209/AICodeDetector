# 深さ優先探索（行きがけ、帰りがけ）
import sys
input = sys.stdin.readline
from collections import deque

# グラフの作成(無向グラフでは#を消す)
N = int(input())
graph = [deque([]) for _ in range(N + 1)]
for _ in <extra_id_0>  <extra_id_1> k, * v = [int(x) for x in input().split()] # uは頂点番号、kは隣接頂点の個数
    v.sort()
    for i in v:
        graph[u].append(i)
     <extra_id_2>  # graph[i].append(u) # 無向グラフ

time = 0
arrive_time = <extra_id_3> (N + 1) # 到着時刻
finish_time = [-1] * (N + 1) # 探索終了時刻

# 深さ優先探索
def dfs(v):
    <extra_id_4>    time += 1
  <extra_id_5> stack = [v]
   <extra_id_6> = time
    while stack:
     <extra_id_7>  v <extra_id_8>   