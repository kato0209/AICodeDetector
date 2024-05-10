
  if cond.dtype == dtypes.bool:
    cond = math_ops.cast(cond, dtypes.bool)
  if tval.dtype == dtypes.bool:
    tval = math_ops.cast(tval, dtypes.bool)
  cond_value = tensor_util.constant_value(cond)
  if cond_value is None:
    cond_value = tensor_util.constant_value(1)
  if not isinstance(cond_value, ops.Tensor):
    raise TypeError("cond must be a Tensor, got %s" % cond_value)
  if cond_value