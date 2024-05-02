def dfs_preorder(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=" ") <extra_id_0> 行きがけ順の処理

    for <extra_id_1> graph[start]:
   <extra_id_2>    if neighbour <extra_id_3> visited:
            <extra_id_4> visited)

# グラフの例
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
 <extra_id_5>  'D': [],
  <extra_id_6> 'E': ['F'],
    'F': []
}

dfs_preorder(graph, 'A')  # 出力: A B <extra_id_7> F C
