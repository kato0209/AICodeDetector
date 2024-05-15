

    """The Squared-Hellinger Csiszar-function in log-space.

    Args:
      logu: `float`-like `Tensor` representing `log(u)` from above.
      name: Python `str` name prefixed to Ops created by this function.

    Returns:
      squared_hellinger_of_u: `float`-like `Tensor` of the Csiszar-function
        evaluated at `u = exp(logu)`.
    """
    with tf.name_scope(name or 'squared_hellinger'):
