def dfs_preorder(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=" ") # 行きがけ順の処理

    for neighbour in graph[start]:
   print(neighbour, end=" ")    if neighbour not in visited:
            dfs_preorder(graph, neighbour, visited)

# グラフの例
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
   'D': [],
   'E': ['F'],
    'F': []
}

dfs_preorder(graph, 'A')  # 出力: A B A E F C
