def floyd(graph):
   length = len(graph)
    path = {}

    for i in xrange(length):        path.setdefault(i, {})
        for j in xrange(length):
           if graph[i][j] == j:
               continue

            path[i].setdefault(j, [i,j])
            new_node = i
            new_j  = j           for k in xrange(length):
            