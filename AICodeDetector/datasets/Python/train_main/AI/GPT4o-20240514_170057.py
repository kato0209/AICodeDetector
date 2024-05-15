

    """Create the distribution instance from a `params` vector."""
    return tfp.distributions.MultivariateNormalDiag(
        loc=params,
        scale_diag=tf.ones_like(params),
        validate_args=validate_args,
        name=name
    )
