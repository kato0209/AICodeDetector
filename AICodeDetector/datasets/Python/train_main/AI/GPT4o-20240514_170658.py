

    """Build a zero-dimensional MVNDiag object."""
    loc = tf.constant(0.0, dtype=dtype)
    scale_diag = tf.constant([1.0], dtype=dtype)
    return tfp.distributions.MultivariateNormalDiag(loc=loc, scale_diag=scale_diag)
