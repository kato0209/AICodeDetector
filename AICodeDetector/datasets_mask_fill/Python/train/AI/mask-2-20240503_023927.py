def dfs_postorder(graph, <extra_id_0>    if visited is None:
        visited = set()

    for neighbour in graph[start]:
        if <extra_id_1> in <extra_id_2>       <extra_id_3>   dfs_postorder(graph, neighbour, visited)

    visited.add(start)
    print(start, end=" ")  # 帰りがけ順の処理

# グラフの例
graph = {
    'A': ['B', 'C'],
  <extra_id_4> 'B': ['D', 'E'],
    <extra_id_5>    'D': [],
   <extra_id_6> ['F'],
    'F': []
}

dfs_postorder(graph, 'A')  # 出力: <extra_id_7> F B C A
