
  with ops.name_scope(name, "norm", [value]) as name:
    if order is None:
      size = array_ops.size(value, out_type=dtypes.int32)
    else:
      size = math_ops.cast(
          array_ops.size(value, out_type=dtypes.int32)[order],
          dtypes.int32)
    return math_ops.sqrt(
        math_ops.reduce_sum(
            math_ops.square(value),
            axis=dims,
            keep_dims=True,
            name=name))


