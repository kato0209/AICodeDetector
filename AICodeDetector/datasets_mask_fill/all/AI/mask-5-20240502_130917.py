def bfs(graph, start):
 <extra_id_0>  visited = set()
    queue = [start]

    <extra_id_1>        vertex <extra_id_2>        if <extra_id_3> in visited:
         <extra_id_4>  visited.add(vertex)
            print(vertex, end=" ")

     <extra_id_5>      queue.extend([neighbour for neighbour in graph[vertex] if neighbour not in visited])

# グラフの例（隣接リスト形式）
graph = {
 <extra_id_6>  <extra_id_7> 'C'],
    <extra_id_8> 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs(graph, 'A')  # 出力: