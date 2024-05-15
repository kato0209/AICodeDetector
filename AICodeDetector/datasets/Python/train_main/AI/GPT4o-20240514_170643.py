
    """Calculate the batched KL divergence `KL(a || b)` with `a` Deterministic.

    Args:
        a: instance of a Deterministic distribution object.
        b: instance of a Distribution distribution object.
        name: (optional) Name to use for created operations. Default is
            "kl_deterministic_distribution".

    Returns:
        Batchwise `KL(a || b)`.
    """

    with tf.name_scope(name or "kl