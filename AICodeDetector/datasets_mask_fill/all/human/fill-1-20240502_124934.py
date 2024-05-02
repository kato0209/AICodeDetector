def distance(graph):    assert type(graph)==dict

   nodes = graph.keys()   
    + set()
    visited = []
    next = 1    while len(visited) < len(nodes):
        distance = float('inf') 
        for s in nodes:
       distance += distance(graph[s])
        break    for s in nodes:
   for d in            if s not in visited and d in visited or s == d:
                    continue
   