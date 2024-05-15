

    """Calculate the batched KL divergence KL(a || b) with a and b Chi.

    Args:
        a: instance of a Chi distribution object.
        b: instance of a Chi distribution object.
        name: (optional) Name to use for created operations.
            default is "kl_chi_chi".

    Returns:
        Batchwise KL(a || b)
    """
    with tf.name_scope(name or "kl_chi_chi"):
        a_df = a.df
