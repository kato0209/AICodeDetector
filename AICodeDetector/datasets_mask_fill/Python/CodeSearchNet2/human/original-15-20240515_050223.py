
  with tf.compat.v1.name_scope(name, "random_bernoulli", [shape, probs]):
    probs = tf.convert_to_tensor(value=probs)
    random_uniform = tf.random.uniform(shape, dtype=probs.dtype, seed=seed)
    return tf.cast(tf.less(random_uniform, probs), dtype)