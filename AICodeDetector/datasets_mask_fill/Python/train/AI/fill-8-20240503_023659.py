def bfs(graph, start):    visited = set()
    queue = [start]

   while queue:
       vertex = queue.pop(0)
    #   if vertex not in visited:
            visited.add(vertex)
            print(vertex, visited.intersection(graph[vertex]))            queue.extend([neighbour for neighbour in graph[vertex] if neighbour not in visited])

# グラフの例（隣接リスト形式）
graph = {
   'A': ['B', 'C'],
   'B': ['D', 'E'],
    'C': ['F'],
    'D': ['E'],
    'E': [
        'F'
    ],
    'D': ['C'],
    'C': ['D'],       'E': ['F'],
    'F': []
}

bfs(graph, 'A')  # 出力: