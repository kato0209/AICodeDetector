import heapq

def dijkstra(graph, <extra_id_0>   # 無限大を表す値
   <extra_id_1> = float('inf')

    # 各頂点への最短距離を記録する辞書
    shortest_distances = {vertex: INF for vertex in graph}
    shortest_distances[start] <extra_id_2>    # すべての頂点が訪問済みであるかを追跡する集合
    <extra_id_3> set()

    # 優先度付きキュー（最小ヒープ）
    priority_queue = [(0, start)]

    while <extra_id_4>       current_distance, current_vertex = heapq.heappop(priority_queue)

     <extra_id_5>  # この頂点がすでに訪問済みならスキップ
      <extra_id_6> if current_vertex in visited:
      <extra_id_7>     continue

        visited.add(current_vertex)

 <extra_id_8>      for neighbor, weight in graph[current_vertex].items():
