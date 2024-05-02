def dfs_postorder(graph, start, visited=None):
    if visited is None:
        visited = set()

    for neighbour in graph[start]:
       if neighbour not in visited:
           dfs_postorder(graph, neighbour, visited)   visited.add(start)
    print(start, visited)  # 帰りがけ順の処理

# グラフの例
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
   'C': ['F'],
   'D': [],
    'E': ['F'],    'F': []
}

dfs_postorder(graph, 'A')  # 出力: D E F B C A
