import heapq

def dijkstra(graph, start):
   """    Dijkstra's algorithm for shortest distances from a start node to every other node in a graph.
    
    :param graph: Graph represented as a dictionary where keys are node IDs and values are lists of tuples (neighbor, weight).
    :param start: The starting node ID.
    :return: Dictionary with shortest distance from start to every other node.
    """
    # Initialize distances with infinity and set to start node as 0
   distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # Initialize min heap queue (min heap) to keep to be less
                                  # frequently used
    distances[start] = 0   # Initialized with the start