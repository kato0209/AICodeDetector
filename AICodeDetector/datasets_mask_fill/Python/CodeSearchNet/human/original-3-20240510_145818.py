
  # Note that `all` defaults to `True` if `arg_list` is empty.
  if all(a is None for a in arg_list):
    return None
  return dtype_util.common_dtype(arg_list, tf.float32)