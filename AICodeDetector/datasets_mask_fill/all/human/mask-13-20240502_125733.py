def floyd(graph):
 <extra_id_0>  length = len(graph)
    path = {}

    for i <extra_id_1>        path.setdefault(i, {})
        for j in xrange(length):
     <extra_id_2>      if <extra_id_3> j:
       <extra_id_4>        continue

            path[i].setdefault(j, [i,j])
            new_node <extra_id_5>         <extra_id_6>  for k in xrange(length):
     <extra_id_7>  <extra_id_8>     