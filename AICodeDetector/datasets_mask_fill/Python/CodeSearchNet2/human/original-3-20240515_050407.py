
  if dims == 0:
    return tf.math.abs(value)
  elif dims == 1:
    axis = -1
  elif dims == 2:
    axis = [-1, -2]
  else:
    ValueError(dims)
  if order is None:
    order = np.inf
  return tf.norm(tensor=value, axis=axis, ord=order)