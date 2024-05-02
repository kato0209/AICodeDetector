def prim(graph, root):
    assert type(graph)==dict

    nodes = graph.keys()
    nodes.remove(root)
    
    visited = [root]
  <extra_id_0> path = []
 <extra_id_1>  next = None

    while nodes:
     <extra_id_2>  distance = float('inf') <extra_id_3>       for s in visited:
    <extra_id_4>     <extra_id_5> for d in graph[s]:
                if d in visited or s == d:
  <extra_id_6>        <extra_id_7>        <extra_id_8>  