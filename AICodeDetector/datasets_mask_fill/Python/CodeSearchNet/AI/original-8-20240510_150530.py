
  shape = array_ops.shape(tensor)
  # Make sure the input tensor is 2D.
  shape[0], shape[1] = shape[1], shape[0]
  tensor = array_ops.reshape(tensor, [-1, shape[2]])
  # Make sure the input has 4 dimensions.
  shape[3], shape[4] = shape[3], shape[4]
  return array_ops.tile(tensor, array_ops.concat(0, [n, n, -1]))


def _squeeze(input, axis=None, name=None,