def kruskal(graph):
    assert type(graph)==dict

    nodes = graph.keys()   
    visited = set()
 <extra_id_0>  path = []
   <extra_id_1> = None

    while len(visited) <extra_id_2>        distance <extra_id_3> 
        for s in nodes:
     <extra_id_4>     <extra_id_5> d in nodes:
          <extra_id_6>     if s in <extra_id_7> d <extra_id_8> or s == d:
                    continue
   