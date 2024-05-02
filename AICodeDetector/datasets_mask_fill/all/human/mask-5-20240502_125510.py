# <extra_id_0> = sys.stdin.readline
from <extra_id_1> deque

# グラフの作成(無向グラフでは#を消す)
N = int(input())
graph = [deque([]) for _ in range(N + 1)]
for _ in range(N):
 <extra_id_2>  u, k, * v = [int(x) for x in input().split()] # uは頂点番号、kは隣接頂点の個数
   <extra_id_3>    for i in v:
   <extra_id_4>    graph[u].append(i)
        # <extra_id_5> 無向グラフ

time = 0
arrive = [-1] * (N + 1) # 到着したか
finish_time <extra_id_6> * (N + 1) # 探索終了時刻

# 深さ優先探索
def dfs(v):
   <extra_id_7> time
    stack = [v]
    arrive[v] = 1
    while stack:
        v = stack[-1]
    <extra_id_8>   if graph[v]:
