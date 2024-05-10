
  if tensorshape is None:
    return None
  if isinstance(tensorshape, ops.Tensor):
    shape = tensorshape.as_shape(tensorshape)
  if not isinstance(shape, ops.Tensor):
    raise TypeError("shape is not a Tensor")
  if shape.ndims is not None:
    return constant_op.constant(
        np.arange(shape.ndims), dtype=dtypes.int32)
  if not shape:
    return constant_op.constant(0, dtype=dtypes.int32)
  return array_ops.rank(shape)


def _as_indexed_