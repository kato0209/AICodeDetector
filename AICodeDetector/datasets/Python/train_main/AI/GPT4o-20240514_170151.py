

    """Calculate the batched KL divergence KL(n_a || n_b) with n_a and n_b Normal.

    Args:
        n_a: instance of a Normal distribution object.
        n_b: instance of a Normal distribution object.
        name: (optional) Name to use for created operations.
            default is "kl_normal_normal".

    Returns:
        Batchwise KL(n_a || n_b)
    """
    with tf.name_scope(name or "kl_normal_normal"):
        mean_a = n_a.mean()
        mean