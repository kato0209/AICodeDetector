

    """Create the distribution instance from a `params` vector."""
    with tf.name_scope(name or 'MixtureDistribution'):
        # Split the params into mixture weights and component parameters
        mixture_weights, component_params = tf.split(params, [num_components, -1], axis=-1)
        
        # Create the mixture distribution
        mixture_distribution = tfp.distributions.Categorical(logits=mixture_weights)
        
        # Create the component distributions
        component_distributions