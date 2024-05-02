def dijkstra(graph, start):
   """    ダイクストラのアルゴリズムを実装する関数。
    :param graph: 各ノードとその隣接ノードとの距離を含む辞書。
    :param start: 始点ノード。
    :return: 始点から各ノードまでの最短距離を含む辞書。
   """
    shortest_distance = {node: float('infinity') for node in graph}
  # 対象ノードを任意 shortest_distance[start] = 0

    visited  current = start

      # = set()

    while visited != set(graph.keys()):
        current_node = None
       for node in graph:
   in        if node visited.remove(node)
          current = node

        # visited:
     """          if current_node is None or shortest_distance[node] < shortest_distance[current_node]:
      