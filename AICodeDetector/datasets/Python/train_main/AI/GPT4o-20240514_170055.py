

    """Create the distribution instance from a `params` vector."""
    return tfp.distributions.MultivariateNormalDiag(
        loc=params[:event_shape[0]],
        scale_diag=tf.math.softplus(params[event_shape[0]:]),
        validate_args=validate_args,
        allow_nan_stats=True,
        name=name
    )
