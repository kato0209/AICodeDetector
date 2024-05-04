from queue import Queue

def bfs(graph, start):
    visited = set()
    queue = Queue()
    queue.put(start)
    visited.add(start)

    while not queue.empty():
        vertex = queue.get()
        print(vertex, end=" ")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                queue.put(neighbour)
                visited.add(neighbour)

# グラフの例（隣接リスト形式）
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs(graph, 'A')  # 出力: A B C D E F
