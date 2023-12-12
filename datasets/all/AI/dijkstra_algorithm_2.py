def dijkstra(graph, start):
    """
    ダイクストラのアルゴリズムを実装する関数。
    :param graph: 各ノードとその隣接ノードとの距離を含む辞書。
    :param start: 始点ノード。
    :return: 始点から各ノードまでの最短距離を含む辞書。
    """
    shortest_distance = {node: float('infinity') for node in graph}
    shortest_distance[start] = 0
    visited = set()

    while visited != set(graph.keys()):
        current_node = None
        for node in graph:
            if node not in visited:
                if current_node is None or shortest_distance[node] < shortest_distance[current_node]:
                    current_node = node

        if current_node is None:
            break

        visited.add(current_node)
        for neighbour, weight in graph[current_node].items():
            distance = shortest_distance[current_node] + weight
            if distance < shortest_distance[neighbour]:
                shortest_distance[neighbour] = distance

    return shortest_distance

# グラフの例
graph_example = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# 始点Aからの最短距離を計算
shortest_distances_from_A = dijkstra(graph_example, 'A')
shortest_distances_from_A
