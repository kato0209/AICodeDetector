

    """Calculate the batched KL divergence KL(a || b) with a and b `HalfNormal`.

    Args:
        a: Instance of a `HalfNormal` distribution object.
        b: Instance of a `HalfNormal` distribution object.
        name: (optional) Name to use for created operations.
            default is "kl_half_normal_half_normal".

    Returns:
        Batchwise KL(a || b)
    """
    with tf.name_scope(name or "kl_half_normal_half_normal