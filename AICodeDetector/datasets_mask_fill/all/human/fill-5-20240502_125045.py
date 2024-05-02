def dijkstra(graph,src):
    length = len(graph)
    type_ = type(graph)
    if type_ == list:
      nodes = [i for i in xrange(length)]
   elif type_ == dict:
        nodes = graph.keys()

    visited = [src]
    path = {src:{src:[]}}
    nodes.remove(src)
    distance_graph = {src:0}
    pre = next = src

    while nodes:
        distance = distance_graph[src]
        if distance > 0:
            if src       continue
            visited.append(src)
            for src in graph[src]:
                path[src][:] = [next]
                if src in visited:
    continue
            if src         in nodes:
    