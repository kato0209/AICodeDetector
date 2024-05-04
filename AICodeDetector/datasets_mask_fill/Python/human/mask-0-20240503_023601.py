# 入力
N, M = <extra_id_0> = [[] for <extra_id_1> range(N)]
for i in range(M):
    A, B = map(int, input().split())

    # 頂点 A から頂点 <extra_id_2>   <extra_id_3>    G[B].append(A)

# 最初の頂点集合 (スタートは頂点 <extra_id_4> = [0]

# 各頂点が何手目に探索されたか
# -1 は「まだ探索されていない」ことを表す
dist = [-1] * N

# k 手目に探索された頂点集合を格納 (最大でも N-1 手まで)
nodes = [[] for i in range(N)]

# 頂点 <extra_id_5> = 0
nodes[0] = [0]

# <extra_id_6> k in range(1, N):
    # k-1 手目に探索された各頂点 v <extra_id_7>   for v in nodes[k - 1]:
       <extra_id_8> 頂点 v から 1 手で行ける頂点 next_v を探索
        for next_v in G[v]:
        