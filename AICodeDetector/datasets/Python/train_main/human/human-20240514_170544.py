
  return tf.reduce_logsumexp(
      input_tensor=2. * tf.math.log(tf.abs(x)), axis=axis)