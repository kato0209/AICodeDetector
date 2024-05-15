
  with tf.name_scope(name or "kl_normal_normal"):
    one = tf.constant(1, dtype=n_a.dtype)
    two = tf.constant(2, dtype=n_a.dtype)
    half = tf.constant(0.5, dtype=n_a.dtype)
    s_a_squared = tf.square(n_a.scale)
    s_b_squared = tf.square(n_b.scale)
    ratio = s_a_squared / s_b_squared
    return (tf.square(n_a.loc - n_b.loc) / (two * s_b_squared) + half *
            (ratio - one - tf.math.log(ratio)))