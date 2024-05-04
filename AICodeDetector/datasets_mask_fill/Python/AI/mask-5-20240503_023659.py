import heapq

def dijkstra(graph, start):
    <extra_id_0>    INF = float('inf')

    # 各頂点への最短距離を記録する辞書
    shortest_distances = {vertex: INF for vertex in graph}
    shortest_distances[start] = 0

    <extra_id_1>    <extra_id_2> set()

    # 優先度付きキュー（最小ヒープ）
    <extra_id_3> [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

      <extra_id_4> # この頂点がすでに訪問済みならスキップ
   <extra_id_5>    if current_vertex in visited:
        <extra_id_6>   continue

    <extra_id_7>   visited.add(current_vertex)

    <extra_id_8>   for neighbor, weight in graph[current_vertex].items():
