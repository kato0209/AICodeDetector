def <extra_id_0>    visited = set()
    queue = [start]

  <extra_id_1> while queue:
       <extra_id_2> = queue.pop(0)
    <extra_id_3>   if vertex not in visited:
            visited.add(vertex)
            print(vertex, <extra_id_4>            queue.extend([neighbour for neighbour in graph[vertex] if neighbour not in visited])

# グラフの例（隣接リスト形式）
graph = {
 <extra_id_5>  'A': ['B', 'C'],
 <extra_id_6>  'B': ['D', 'E'],
    'C': <extra_id_7>   <extra_id_8>    'E': ['F'],
    'F': []
}

bfs(graph, 'A')  # 出力: