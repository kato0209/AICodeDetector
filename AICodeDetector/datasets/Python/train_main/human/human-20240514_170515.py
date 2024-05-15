
  if not dtype_util.is_integer(shape.dtype):
    raise TypeError('{} dtype ({}) should be `int`-like.'.format(
        shape, dtype_util.name(shape.dtype)))

  assertions = []

  message = '`{}` rank should be <= 1.'
  if tensorshape_util.rank(shape.shape) is not None:
    if tensorshape_util.rank(shape.shape) > 1:
      raise ValueError(message.format(shape))
  elif validate_args:
    assertions.append(assert_util.assert_less(
        tf.rank(shape), 2, message=message.format(shape)))

  shape_ = tf.get_static_value(shape)

  message = '`{}` elements must have at most one `-1`.'
  if shape_ is not None:
    if sum(shape_ == -1) > 1:
      raise ValueError(message.format(shape))
  elif validate_args:
    assertions.append(assert_util.assert_less(
        tf.reduce_sum(input_tensor=tf.cast(tf.equal(shape, -1), tf.int32)),
