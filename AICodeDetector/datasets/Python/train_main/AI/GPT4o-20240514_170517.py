

    """Calculate the batchwise KL divergence KL(d1 || d2) with d1 and d2 Beta.

    Args:
        d1: instance of a Beta distribution object.
        d2: instance of a Beta distribution object.
        name: (optional) Name to use for created operations.
            default is "kl_beta_beta".

    Returns:
        Batchwise KL(d1 || d2)
    """
    with tf.name_scope(name or "kl_beta_beta"):
        return (