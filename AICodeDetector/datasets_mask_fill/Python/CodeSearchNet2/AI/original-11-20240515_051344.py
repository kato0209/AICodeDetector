
    override_shape = ops.convert_to_tensor(override_shape, dtype=dtypes.int32,
                                           name="override_shape")
    if override_shape.get_shape().ndims is not None and override_shape.get_shape().ndims < 1:
      raise ValueError("Shape override must be at least 1.")
    if override_shape.get_shape().ndims is not None and override_shape.get_shape().ndims!= 1:
      raise ValueError("Shape override must be a scalar, received shape: %s" %
                       override_shape)
  