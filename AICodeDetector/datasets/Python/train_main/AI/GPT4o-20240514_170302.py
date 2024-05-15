

    """Computes the multivariate digamma function; Psi_p(a)."""
    with tf.name_scope(name):
        a = tf.convert_to_tensor(a, name="a")
        p = tf.convert_to_tensor(p, name="p")
        return tf.reduce_sum(tf.math.digamma(a - tf.range(p, dtype=a.dtype) / 2), axis=-1)
