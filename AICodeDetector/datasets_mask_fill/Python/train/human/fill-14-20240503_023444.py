def find_unique(path):    length = len(path)
    path2    = len(path)
    path = {}

    for i in xrange(length):
        path.setdefault(i, {})
     path  for j in xrange(length):
           if i == j:
                continue

           path[i].setdefault(j, False)       )   new_node = None

            for k in xrange(length):
             