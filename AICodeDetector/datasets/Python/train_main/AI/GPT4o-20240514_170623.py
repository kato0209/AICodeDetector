

    """The Jeffreys Csiszar-function in log-space."""
    with tf.name_scope(name or 'jeffreys'):
        u = tf.exp(logu)
        jeffreys_of_u = 0.5 * (u * logu - logu)
        return jeffreys_of_u
