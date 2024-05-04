def dijkstra(graph, <extra_id_0>   """
    <extra_id_1>   :param graph: 各ノードとその隣接ノードとの距離を含む辞書。
    :param start: 始点ノード。
    <extra_id_2>    """
   <extra_id_3> = {node: float('infinity') for node <extra_id_4>    shortest_distance[start] = 0
  <extra_id_5> visited = set()

    while visited != set(graph.keys()):
        current_node = None
  <extra_id_6>     for node in graph:
         <extra_id_7>  if node not in visited:
            <extra_id_8>   if current_node is None or shortest_distance[node] < shortest_distance[current_node]:
      