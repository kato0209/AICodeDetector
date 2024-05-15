

  with tf.compat.v1.name_scope(name, "triangular", [logu]):
    logu = tf.convert_to_tensor(value=logu, name="logu")
    return pearson(logu) / (1. + tf.exp(logu))