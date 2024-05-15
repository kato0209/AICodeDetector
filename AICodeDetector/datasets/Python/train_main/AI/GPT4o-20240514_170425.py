

    """Calculate the batched KL divergence KL(a || b) with a and b Laplace.

    Args:
        a: instance of a Laplace distribution object.
        b: instance of a Laplace distribution object.
        name: (optional) Name to use for created operations.
            default is "kl_laplace_laplace".

    Returns:
        Batchwise KL(a || b)
    """
    with tf.name_scope(name or "kl_laplace_laplace"):
        # Extract the parameters