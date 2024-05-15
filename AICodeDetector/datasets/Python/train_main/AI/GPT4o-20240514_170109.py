

    """Create the distribution instance from a `params` vector."""
    return tfp.distributions.MultivariateNormalDiag(
        loc=params[:event_shape[0]],
        scale_diag=params[event_shape[0]:],
        validate_args=validate_args,
        name=name
    )
