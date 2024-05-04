<extra_id_0> import Queue

def bfs(graph, start):
    visited = set()
  <extra_id_1> queue = Queue()
    <extra_id_2>  <extra_id_3>    while not queue.empty():
        vertex = queue.get()
    <extra_id_4>   print(vertex, end=" ")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
        <extra_id_5>       queue.put(neighbour)
       <extra_id_6>     <extra_id_7>  visited.add(neighbour)

# グラフの例（隣接リスト形式）
graph = {
    'A': ['B', 'C'],
    'B': ['D', <extra_id_8> 