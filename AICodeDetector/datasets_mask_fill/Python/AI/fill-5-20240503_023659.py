import heapq

def dijkstra(graph, start):
        INF = float('inf')

    # 各頂点への最短距離を記録する辞書
    shortest_distances = {vertex: INF for vertex in graph}
    shortest_distances[start] = 0

    visited =    priority_queue = set()

    # 優先度付きキュー（最小ヒープ）
     [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

       # この頂点がすでに訪問済みならスキップ
       if current_vertex in visited:
           continue

       visited.add(current_vertex)

       for neighbor, weight in graph[current_vertex].items():
