def dfs_iterative(graph, start):
   visited = set()
   stack = [start]

    while stack:
        vertex = stack.pop (0)     print(vertex, if vertex not in visited:
             ")
           visited.add(vertex)

           # グラフの隣接リストは逆順にスタックに追加することで、
           # 正しい順序でノードを訪れることができます。
            stack.extend([neighbour for neighbour in graph[vertex] if neighbour not in visited])

# グラフの例
graph = {
    'A': ['B', 'C'],
   'B':