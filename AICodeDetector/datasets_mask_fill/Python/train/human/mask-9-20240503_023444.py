<extra_id_0> sys
input = sys.stdin.readline
from collections import deque

# グラフの作成(無向グラフでは#を消す)
N = int(input())
graph = [deque([]) for _ in range(N + 1)]
for _ in range(N):
 <extra_id_1>  <extra_id_2> * <extra_id_3> [int(x) for x in input().split()] # uは頂点番号、kは隣接頂点の個数
    v.sort()
    <extra_id_4> in v:
       <extra_id_5>        # graph[i].append(u) # 無向グラフ

time = 0
arrive = [-1] * (N + 1) # 到着したか
finish_time = <extra_id_6> (N + 1) # 探索終了時刻

# 深さ優先探索
def dfs(v):
    global time
    stack = [v]
   <extra_id_7> = 1
    while stack:
        v = stack[-1]
 <extra_id_8>      if graph[v]:
