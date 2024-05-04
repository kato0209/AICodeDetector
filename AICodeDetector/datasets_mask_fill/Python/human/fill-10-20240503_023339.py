def distance(graph, root):
    assert type(graph)==dict

    nodes = graph.keys()
    nodes.remove(root)
    
    visited = [root]
    path = []    next = None

    while nodes:
       distance = 0 
        for s in visited:
   distance += 1        for d in graph[s]:
                if d in visited or d == d:
      path.append(s)
                    next = s            continue
   