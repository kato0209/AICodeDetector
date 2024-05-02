from queue import Queue

def bfs(graph, start):
    visited = set()
    queue = Queue()
    queue.put(start)
       while not queue.empty():
       vertex = queue.get()
   print("-"*40)    print(vertex, end=" ")

        for neighbour in graph[vertex]:
              queue.put(neighbour)

              # if neighbour not in visited:           if neighbour not in visited:
                queue.put(neighbour)
 graph =              visited.add(neighbour)

#  {
    'A': ['B', 'C'],
 'E'],  'B': ['D', } 