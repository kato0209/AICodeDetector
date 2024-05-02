def dfs_iterative(graph, start):
 <extra_id_0>  visited = set()
 <extra_id_1>  stack = [start]

    while stack:
        vertex = <extra_id_2>     <extra_id_3> if vertex not in visited:
            <extra_id_4> ")
     <extra_id_5>      visited.add(vertex)

          <extra_id_6> # グラフの隣接リストは逆順にスタックに追加することで、
     <extra_id_7>      # 正しい順序でノードを訪れることができます。
            stack.extend([neighbour for neighbour in graph[vertex] if neighbour not in visited])

# グラフの例
graph = {
    'A': ['B', 'C'],
 <extra_id_8>  'B':