<extra_id_0> root):
    assert type(graph)==dict

    nodes = graph.keys()
    nodes.remove(root)
    
    visited = [root]
    path <extra_id_1>    next = None

    while nodes:
      <extra_id_2> distance <extra_id_3> 
        for s in visited:
   <extra_id_4>        for <extra_id_5> graph[s]:
                if d in visited <extra_id_6> == d:
      <extra_id_7>           <extra_id_8> continue
   