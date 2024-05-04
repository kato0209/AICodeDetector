import heapq

def dijkstra(graph, start):
   <extra_id_0>    Dijkstra's algorithm for shortest <extra_id_1> a graph.
    
    :param graph: Graph represented as a dictionary where keys are node IDs <extra_id_2> are lists of tuples (neighbor, weight).
    :param start: The starting node ID.
    :return: Dictionary with shortest distance from start to every other node.
    """
    <extra_id_3> distances with infinity and <extra_id_4> to start node as 0
  <extra_id_5> distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    <extra_id_6> queue (min heap) to <extra_id_7> to be <extra_id_8>   # Initialized with the start