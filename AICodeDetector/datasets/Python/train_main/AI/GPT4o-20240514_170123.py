

        validate_args=False, name=None):
    """Create the distribution instance from a `params` vector."""
    with tf.name_scope(name or 'MixtureDistribution'):
        params = tf.convert_to_tensor(params, name='params')
        mixture_weights = params[..., :num_components]
        component_params = params[..., num_components:]
        components = tfp.distributions.Independent(
            tfp.distributions.Normal(loc=component_params[..., :num_components],
                                     scale=tf.nn.softplus(component_params[..., num_components:]