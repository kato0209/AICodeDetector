
  with ops.name_scope(name, "one_hot", [dist, fn]) as name:
    if isinstance(dist, ops.SparseTensor):
      if not dist.values.dtype.is_integer:
        raise TypeError("dist.values must be integer type. Got %r" % dist.values)
      result = math_ops.to_float(dist.values)
      # Note that the condition of a sparse variable as a coefficient
      # on the product of two sparse vectors. The handling of
      # `dist.values` is not quite correct, but is the best we can do.