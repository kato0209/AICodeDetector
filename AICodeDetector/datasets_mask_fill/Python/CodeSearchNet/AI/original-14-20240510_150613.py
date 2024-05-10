
  if fn_arg_list is None:
    fn_arg_list = nest.flatten(fn_arg_list)

  fn_name = fn.__name__
  if hasattr(fn, "__name__"):
    fn_name = fn.__name__

  # TODO(josh11b): Make sure we are not mutating the argument types from
  # functions.
  for i, arg in enumerate(fn_arg_list):
    if isinstance(arg, ops.Tensor):
      if context.executing_eagerly():
        arg_name = arg.op.name
        i = i + 1
     