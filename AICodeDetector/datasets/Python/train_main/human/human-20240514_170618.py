
  for i in sorted(axis):
    x = tf.expand_dims(x, axis=i)
  return x