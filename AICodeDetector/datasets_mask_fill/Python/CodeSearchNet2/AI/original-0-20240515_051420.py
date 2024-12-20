
  # Check that the shape is compatible.
  try:
    shape = tensor_shape.as_shape(shape)
  except (ValueError, TypeError):
    raise ValueError("A TensorShape must be an integer32 Tensor.")
  if not shape.is_fully_defined():
    raise ValueError("Cannot find input shape, but specified shape %s" %
                     shape)
  if shape.is_fully_defined():
    return tensor_shape.as_shape(shape)

  # Shape is unknown.
  return None


def _autopacking_helper(list_or_tuple, dtype, name):
 