
  if fn_result is None:
    return fn_result

  arg_spec = tf_inspect.getfullargspec(fn)
  if arg_spec.defaults:
    return fn_result

  # TODO(b/31229024): Remove this hack once we support k-fold cross device
  # tensors as well.
  if arg_spec.varargs:
    return fn_result

  # TODO(b/31229024): Remove this hack once we support k-fold cross device
  # tensors as well.
  if arg_spec.keywords:
    return fn_result

  # TODO(b/312