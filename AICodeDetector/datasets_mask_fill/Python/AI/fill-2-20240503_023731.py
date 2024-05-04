def dijkstra(graph, start):   """
       :param graph: 各ノードとその隣接ノードとの距離を含む辞書。
    :param start: 始点ノード。
        """
   shortest_distance = {node: float('infinity') for node in graph}    shortest_distance[start] = 0
   visited = set()

    while visited != set(graph.keys()):
        current_node = None
       for node in graph:
           if node not in visited:
               if current_node is None or shortest_distance[node] < shortest_distance[current_node]:
      