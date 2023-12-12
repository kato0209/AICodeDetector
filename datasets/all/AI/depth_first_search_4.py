def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)

            # グラフの隣接リストは逆順にスタックに追加することで、
            # 正しい順序でノードを訪れることができます。
            stack.extend([neighbour for neighbour in graph[vertex] if neighbour not in visited])

# グラフの例
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

dfs_iterative(graph, 'A')  # 出力: A C F B E D
