

    """Calculate the batched KL divergence KL(g0 || g1) with g0 and g1 Gamma.

    Args:
        g0: instance of a Gamma distribution object.
        g1: instance of a Gamma distribution object.
        name: (optional) Name to use for created operations. Default is
          "kl_gamma_gamma".

    Returns:
        kl_gamma_gamma: `Tensor`. The batchwise KL(g0 || g1).
    """
    with tf.name_scope(name