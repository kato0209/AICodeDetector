<extra_id_0>    length <extra_id_1>    <extra_id_2> {}

    for i in xrange(length):
        path.setdefault(i, {})
     <extra_id_3>  for j in xrange(length):
    <extra_id_4>       if i == j:
                continue

      <extra_id_5>     path[i].setdefault(j, <extra_id_6>       <extra_id_7>   new_node = None

            for k in xrange(length):
  <extra_id_8>           