

  with tf.compat.v1.name_scope(name, "squared_hellinger", [logu]):
    logu = tf.convert_to_tensor(value=logu, name="logu")
    return pearson(0.5 * logu)