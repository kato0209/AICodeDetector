
  if fn_arg_list is None:
    fn_arg_list = nest.flatten(fn_args)

  if grads is None:
    grads = fn_arg_list[0]  # Returns a list of no gradients, one element per output.

  # TODO(zhifengc): Consider adding support for broadcasting Tensors passed as
  # inputs.
  if check_non_none_grads:
    grads = [g for g in grads if g is not None]
  # TODO(zhifengc): Consider adding support for broadcasting Tensors passed as
  # inputs.
  if len(fn