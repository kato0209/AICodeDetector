
  if isinstance(values, (list, tuple)):
    for i, v in enumerate(values):
      if isinstance(v, ops.Tensor):
        tf.Print(i, v.name, **v.as_list())
      else:
        tf.Print(i, v, **v.as_list())
  elif isinstance(values, (tuple, list)):
    tf.Print(values, **values)
  else:
    tf.Print(values, **values)


def _is_tensor_or_tensor_list(v):
  return isinstance(v, (ops.Tensor