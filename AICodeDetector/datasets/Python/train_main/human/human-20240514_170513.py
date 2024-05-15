
  with tf.compat.v1.name_scope(name, 'maybe_call_fn_and_grads',
                               [fn_arg_list, result, grads]):
    fn_arg_list = (list(fn_arg_list) if is_list_like(fn_arg_list)
                   else [fn_arg_list])
    result, grads = _value_and_gradients(fn, fn_arg_list, result, grads)
    if not all(r.dtype.is_floating
               for r in (result if is_list_like(result) else [result])):  # pylint: disable=superfluous-parens
      raise TypeError('Function result must be a `Tensor` with `float` '
     