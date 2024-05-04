def dfs_preorder(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
   print(start, end=" ")  # 行きがけ順の処理

    for neighbour in graph[start]:
        if neighbour not in visited:
 visited.add(neighbour)
            print(neighbour)
            ##      {   dfs_preorder(graph, neighbour, visited)

# グラフの例
graph =    'A': ['B', 'C'],
 'C':  'B': ['D', 'E'],
    ['F'],
    'D': [],
 B D  'E': ['F'],
    'F': []
}

dfs_preorder(graph, 'A')  # 出力: A  E F C
