# <extra_id_0> = sys.stdin.readline
from collections <extra_id_1> グラフの作成(無向グラフでは#を消す)
N = int(input())
graph = [deque([]) for _ in range(N + 1)]
for _ in range(N):
    <extra_id_2> * v = [int(x) for x in input().split()] # uは頂点番号、kは隣接頂点の個数
    v.sort()
 <extra_id_3>  for i in v:
       <extra_id_4>        # graph[i].append(u) # 無向グラフ

time = 0
arrive_time = [-1] * (N + 1) # 到着時刻
finish_time <extra_id_5> * (N + 1) # 探索終了時刻

# 深さ優先探索
def dfs(v):
    global <extra_id_6>   time += 1
 <extra_id_7>  stack = [v]
    arrive_time[v] <extra_id_8>    while stack:
        v = stack[-1]
   