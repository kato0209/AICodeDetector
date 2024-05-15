
  values = tf.convert_to_tensor(value=values, name='values')
  values_ = tf.get_static_value(values)

  # Static didn't work.
  if values_ is None:
    # Cheap way to bring to at least 1d.
    return values + tf.zeros([1], dtype=values.dtype)

  # Static worked!
  if values_.ndim > 1:
    raise ValueError('values had > 1 dim: {}'.format(values_.shape))
  # Cheap way to bring to at least 1d.
  values_ = values_ + np.zeros([1], dtype=values_.dtype)
  return list(values_)