def dijkstra(graph,src):
    length = len(graph)
    type_ = type(graph)
    if type_ == list:
  <extra_id_0>   <extra_id_1> nodes = [i for i in xrange(length)]
  <extra_id_2> elif <extra_id_3> dict:
        <extra_id_4> graph.keys()

    visited = [src]
    path = {src:{src:[]}}
    nodes.remove(src)
    distance_graph = {src:0}
    pre = next = src

    while nodes:
        distance = <extra_id_5>       <extra_id_6> in visited:
    <extra_id_7>        <extra_id_8> in nodes:
    