
  if not validate_args:
    return

  if name is None:
    name = "rightmost_transposed_ndims"
  with ops.name_scope(name) as name:
    rightmost_dims = ops.convert_to_tensor(rightmost_transposed_ndims,
                                            name="rightmost_dims")
    if rightmost_dims.shape.ndims!= 0:
      raise ValueError("Expected rightmost_dims to have known rank, "
                       "received shape: %s" % rightmost_dims.shape)

  if rightmost_dims.shape[-1].value!= 1