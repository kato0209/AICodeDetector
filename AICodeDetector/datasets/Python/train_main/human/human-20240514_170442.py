
  a = tf.convert_to_tensor(value=a, name="a")
  b = tf.convert_to_tensor(value=b, name="b")

  # Here we can't just do tf.equal(a.shape, b.shape), since
  # static shape inference may break the equality comparison between
  # shape(a) and shape(b) in tf.equal.
  def all_shapes_equal():
    return tf.reduce_all(
        input_tensor=tf.equal(
            tf.concat([tf.shape(input=a), tf.shape(input=b)], 0),
            tf.concat([tf.shape(input=b), tf.shape(input=a)], 0)))

  # One of the shapes isn't fully defined, so we need to use the dynamic
  # shape.
  return tf.cond(
      pred=tf.equal(tf.rank(a), tf.rank(b)),
      true_fn=all_shapes_equal,
      false_fn=lambda: tf.constant(False))