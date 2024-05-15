
  # The maximum iterations permitted are determined as the number of halvings
  # it takes to reduce 1 to 0 in the given dtype.
  iter_max = np.ceil(-np.log2(_machine_eps(val_c_input.x.dtype)))

  def _cond(i, val_c, to_fix):
    del val_c  # Unused.
    return (i < iter_max) & tf.reduce_any(input_tensor=to_fix)

  def _body(i, val_c, to_fix):
    next_c = tf.where(to_fix, val_c.x * step_size_shrink_param, val_c.x)
    next_val_c = value_and_gradients_function(next_c)
    still_to_fix = to_fix & ~hzl.is_finite(next_val_c)
    return (i + 1, next_val_c, still_to_fix)

  to_fix = active & ~hzl.is_finite(val_c_input)
  return tf.while_loop(
      cond=_cond, body=_body, loop_vars=(0, val_c_input, to_fix))