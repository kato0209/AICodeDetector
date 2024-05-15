
  with tf.name_scope(name or 'bernoulli_sample'):
    shape = tf.convert_to_tensor(shape, dtype=dtype, name='shape')
    probs = tf.convert_to_tensor(probs, dtype=dtype, name='probs')
    seed1, seed2 = random_seed.get_seed(seed)
    return tf.random.bernoulli(probs, shape=shape, seed=seed1, dtype=dtype)


def _random_uniform(shape, minval=0.0, maxval=1.0, dtype=tf.float32,