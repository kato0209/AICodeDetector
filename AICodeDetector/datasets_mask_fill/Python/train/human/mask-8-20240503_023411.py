def dijkstra(graph,src):
   <extra_id_0> = len(graph)
    type_ = type(graph)
 <extra_id_1>  if type_ == list:
        nodes = [i for i in xrange(length)]
  <extra_id_2> elif type_ == dict:
       <extra_id_3> = graph.keys()

    visited = [src]
    <extra_id_4> {src:{src:[]}}
    nodes.remove(src)
    distance_graph = {src:0}
    pre = next = src

    while nodes:
     <extra_id_5>  distance = float('inf')
 <extra_id_6>      for v in visited:
   <extra_id_7>         for d in <extra_id_8>   