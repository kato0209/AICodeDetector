
  if static_target_shape is not None:
    if not static_target_shape.is_fully_defined():
      raise ValueError('\'static_target_shape\' must be fully defined.')
    if not static_target_shape.is_compatible_with(dynamic_shape):
      raise ValueError('\'dynamic_shape\' must be fully defined.')
    if dynamic_target_shape.dims is None:
      raise ValueError('\'dynamic_target_shape\' must have known statically '
                       'dynamic shape.')
  else:
    dynamic_target_shape = array_ops.shape(dynamic_target