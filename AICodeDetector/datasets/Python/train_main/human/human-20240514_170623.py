

  with tf.compat.v1.name_scope(name, "jeffreys", [logu]):
    logu = tf.convert_to_tensor(value=logu, name="logu")
    return 0.5 * tf.math.expm1(logu) * logu