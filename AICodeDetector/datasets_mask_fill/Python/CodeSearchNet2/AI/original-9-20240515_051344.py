
  with ops.name_scope(name, "kl_laplace_laplace", values=[a.op, b.op]):
    # Result from:
    # https://en.wikipedia.org/wiki/Batchwise_kl_divergence
    #   Batchwise KL(a || b) = sum_{i=0}^N p_i * p_j^j
    #   where N is batch size and M is number of classes.
    a_shape = a.get_shape()
    b_shape = b.get_shape()
    ndims = a_shape.ndims