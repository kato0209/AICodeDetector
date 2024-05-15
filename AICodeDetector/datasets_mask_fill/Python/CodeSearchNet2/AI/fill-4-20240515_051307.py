
  x_shape = array_ops.shape(x)
  x_rank = array_ops.rank(x)
  y = array_ops.reshape(
      math_ops.reduce_prod(array_ops.shape(x)) / x_shape[x_rank:], [1])
  x_shape = array_ops.shape(x)
  y_rank = array_ops.rank(y)
  x_tail = array_ops.reshape(
      math_ops.reduce_prod(array_ops.shape(y)) / y_shape[y_rank:], [-