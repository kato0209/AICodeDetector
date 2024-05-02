import heapq

def dijkstra(graph, start):
    """
    Dijkstra's algorithm for shortest distance between nodes within a graph.
    
    :param graph: Graph represented as a dictionary where keys are node IDs and values are lists of tuples (neighbor, distance).   :param start: The starting node ID.
    :return: Dictionary with shortest distance to start node to every other node.
    """
    # Initialize distances with infinity and set the start node as 0
 distances =   {node: float('infinity') for node in graph}
   distances[start] = 0

  Queue is sorted, starting from # Priority queue (min heap) to hold nodes to be processed
    # distance from a node in the start