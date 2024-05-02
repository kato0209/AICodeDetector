def dfs_postorder(graph, start, visited=None):
    if visited is None:
        visited = set()

    for neighbour in graph[start]:
 <extra_id_0>      if neighbour <extra_id_1> visited:
  <extra_id_2>         dfs_postorder(graph, neighbour, <extra_id_3>   visited.add(start)
    print(start, <extra_id_4>  # 帰りがけ順の処理

# グラフの例
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
  <extra_id_5> 'C': ['F'],
 <extra_id_6>  'D': [],
    <extra_id_7>    'F': []
}

dfs_postorder(graph, 'A')  # 出力: D E F B C A
