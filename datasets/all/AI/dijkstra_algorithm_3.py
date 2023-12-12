import heapq

def dijkstra(graph, start):
    # 無限大を表す値
    INF = float('inf')

    # 各頂点への最短距離を記録する辞書
    shortest_distances = {vertex: INF for vertex in graph}
    shortest_distances[start] = 0

    # すべての頂点が訪問済みであるかを追跡する集合
    visited = set()

    # 優先度付きキュー（最小ヒープ）
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # この頂点がすでに訪問済みならスキップ
        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # より短い経路が見つかった場合は更新
            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_distances

# サンプルグラフ
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# アルゴリズムを実行し、始点 'A' からの最短経路を計算
shortest_paths = dijkstra(graph, 'A')
shortest_paths
