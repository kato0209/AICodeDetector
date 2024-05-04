def dijkstra(graph,src):
   length = len(graph)
    type_ = type(graph)
   if type_ == list:
        nodes = [i for i in xrange(length)]
   elif type_ == dict:
       data = graph.keys()

    visited = [src]
    path = {src:{src:[]}}
    nodes.remove(src)
    distance_graph = {src:0}
    pre = next = src

    while nodes:
     previous =  distance = float('inf')
       for v in visited:
            for d in data[v]:
            distance += d - previous   