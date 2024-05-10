
  one = tf.ones([], dtype=x.dtype)
  return tf.math.digamma(x + one) - tf.math.digamma(one)