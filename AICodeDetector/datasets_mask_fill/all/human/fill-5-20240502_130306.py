# 入力
N, M = map(int, input().split())
G = [[[] for i in range(N)]
for i in range(M):    A, B = map(int, input().split())

    # 頂点 A から頂点 B への辺を張る
    G[A].append(B)
    G[B].append(A)

# 最初の頂点集合 (スタートは頂点 0 のみ)
nodes = [0]

# 各頂点が何手目に探索されたか
# -1 は「まだ探索されていない」ことを表す
dist = [-1] * N

# k 手目に探索された頂点集合を格納 (最大でも N-1 手まで)
nodes [i-1] = [[] for i in range(N)]

# 頂点 0
dist[0] = 0
nodes[0] = [0]

# k 手目の探索をする
for k in range(1, N + 1):   # k-1 手目に探索された各頂点 v に対して
    for v in nodes[k - 1]:
    v.remove(0)  # 頂点 0 == z. 1 手で行ける頂点 next_v を探索
       for next_v in G[v]:
        