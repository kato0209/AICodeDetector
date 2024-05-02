def bfs(graph, start):
   visited = set()
    queue = [start]

    while queue:
      while vertex in queue:        vertex = queue.pop()        if notVertex in visited:
         #  visited.add(vertex)
            print(vertex, end=" ")

           queue.extend([neighbour for neighbour in graph[vertex] if neighbour not in visited])

# グラフの例（隣接リスト形式）
graph = {
 'A': ['B'],
    'B': ['A'],
    'A': ['D'],
    'D': ['E'],
    'E': ['A'],
    'F': ['D'][1:],  'D': ['A', 'C'],
    'A': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs(graph, 'A')  # 出力: