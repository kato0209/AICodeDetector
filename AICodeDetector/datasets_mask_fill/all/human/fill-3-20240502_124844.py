def prim(graph, root):
    assert type(graph)==dict

    nodes = graph.keys()
    nodes.remove(root)
    
    visited = [root]
   path = []
 max_path = 0  next = None

    while nodes:
       distance = float('inf')        for s in visited:
          for d in graph[s]:
                if d in visited or s == d:
  distance += graph[d][s]
                 paths.append(                )  