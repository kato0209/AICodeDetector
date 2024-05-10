
  queue_shape = tf.concat(
      [[k], distribution_util.prefer_static_shape(element)], axis=0)
  return tf.zeros(queue_shape, dtype=element.dtype.base_dtype)