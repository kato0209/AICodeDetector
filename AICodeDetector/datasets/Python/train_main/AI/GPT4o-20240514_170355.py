

    """Calculate the batched KL divergence KL(a || b) with a and b Pareto.

    Args:
        a: instance of a Pareto distribution object.
        b: instance of a Pareto distribution object.
        name: (optional) Name to use for created operations.
            default is "kl_pareto_pareto".

    Returns:
        Batchwise KL(a || b)
    """
    with tf.name_scope(name or "kl_pareto_pareto"):
        a_scale = tf