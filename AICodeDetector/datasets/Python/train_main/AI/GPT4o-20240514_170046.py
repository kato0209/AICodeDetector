

    """Create the distribution instance from a `params` vector."""
    return tfp.distributions.MultivariateNormalDiag(
        loc=params[..., :event_size],
        scale_diag=tf.nn.softplus(params[..., event_size:]),
        validate_args=validate_args,
        name=name
    )
