import heapq

def dijkstra(graph, start):
    """
    Dijkstra's algorithm for shortest <extra_id_0> a graph.
    
    :param graph: Graph represented as a dictionary where keys are node IDs and values are lists of tuples (neighbor, <extra_id_1>   :param start: The starting node ID.
    :return: Dictionary with shortest distance <extra_id_2> to every other node.
    """
    # Initialize distances with infinity and set <extra_id_3> start node as 0
 <extra_id_4>  <extra_id_5> {node: float('infinity') for node in graph}
  <extra_id_6> distances[start] = 0

  <extra_id_7> # Priority queue (min heap) to hold nodes to be processed
    # <extra_id_8> the start