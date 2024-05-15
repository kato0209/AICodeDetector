

  # tensor dim -> new_dim
  new_dim_static = tensor_util.constant_value(new_shape)
  original_shape_static = tensor_shape.TensorShape(original_shape)
  new_shape_static = tensor_shape.TensorShape(new_shape)

  # 0-D tensor or scalar
  if (original_shape_static is not None and
      original_shape_static!= new_shape_static):
    if validate:
      raise ValueError("Cannot reshape a tensor with %s, but specified shape %s "
                       "and new shape %s "
                       "%s."