

tfd = tfp.distributions

    """Create the distribution instance from a `params` vector."""
    if dtype is None:
        dtype = tf.float32

    params = tf.convert_to_tensor(params, dtype=dtype, name="params")
    loc = params[..., :event_size]
    scale_diag = tf.nn.softplus(params[..., event_size:])

    return tfd.MultivariateNormalDiag(
        loc=loc,
        scale_diag=scale_diag,
       