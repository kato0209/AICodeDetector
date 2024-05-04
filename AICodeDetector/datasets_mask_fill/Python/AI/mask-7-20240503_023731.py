def dfs_preorder(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
 <extra_id_0>  print(start, end=" ")  # 行きがけ順の処理

    for neighbour in graph[start]:
        if neighbour not in visited:
 <extra_id_1>      <extra_id_2>   dfs_preorder(graph, neighbour, visited)

# グラフの例
graph = <extra_id_3>   'A': ['B', 'C'],
 <extra_id_4>  'B': ['D', 'E'],
   <extra_id_5> ['F'],
    'D': [],
 <extra_id_6>  'E': ['F'],
    'F': []
}

dfs_preorder(graph, 'A')  # 出力: A <extra_id_7> E F C
