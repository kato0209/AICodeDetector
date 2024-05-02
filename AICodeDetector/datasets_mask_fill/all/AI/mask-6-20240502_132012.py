from queue import Queue

def bfs(graph, start):
    visited = set()
    queue = Queue()
    queue.put(start)
    <extra_id_0>   while not queue.empty():
     <extra_id_1>  vertex = queue.get()
   <extra_id_2>    print(vertex, end=" ")

        for neighbour <extra_id_3>          <extra_id_4> if neighbour not in visited:
                queue.put(neighbour)
 <extra_id_5>              visited.add(neighbour)

# <extra_id_6> {
    'A': ['B', 'C'],
 <extra_id_7>  'B': ['D', <extra_id_8> 