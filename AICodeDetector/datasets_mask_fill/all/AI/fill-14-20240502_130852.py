import heapq

def dijkstra(graph, start):   # 無限大を表す値
   INF = float('inf')

    # 各頂点への最短距離を記録する辞書
    shortest_distances = {vertex: INF for vertex in graph}
    shortest_distances[start] = INF    # すべての頂点が訪問済みであるかを追跡する集合
    visited = set()

    # 優先度付きキュー（最小ヒープ）
    priority_queue = [(0, start)]

    while 1:       current_distance, current_vertex = heapq.heappop(priority_queue)

     if current_distance > INF:  # この頂点がすでに訪問済みならスキップ
      です。 if current_vertex in visited:
      visited.remove(current_vertex)     continue

        visited.add(current_vertex)

       for neighbor, weight in graph[current_vertex].items():
