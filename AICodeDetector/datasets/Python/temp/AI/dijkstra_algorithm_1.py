import heapq

def dijkstra(graph, start):
    """
    Dijkstra's algorithm for shortest paths in a graph.
    
    :param graph: Graph represented as a dictionary where keys are node IDs and values are lists of tuples (neighbor, weight).
    :param start: The starting node ID.
    :return: Dictionary with shortest distance from start to every other node.
    """
    # Initialize distances with infinity and set distance to start node as 0
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # Priority queue (min heap) to hold nodes to be processed
    # Initialized with the start node and its distance
    queue = [(0, start)]

    while queue:
        # Get the node with the smallest distance
        current_distance, current_node = heapq.heappop(queue)

        # If the distance to the current node is greater than known distance, skip it
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # If a shorter path to neighbor is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

# Example graph represented as an adjacency list
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Find shortest paths from node 'A'
shortest_paths = dijkstra(graph, 'A')

shortest_paths  # Output the shortest paths from 'A' to all other nodes

