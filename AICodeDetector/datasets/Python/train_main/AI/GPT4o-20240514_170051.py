

    """Create the distribution instance from a `params` vector."""
    if dtype is None:
        dtype = tf.float32

    params = tf.convert_to_tensor(params, dtype=dtype, name="params")
    with tf.name_scope(name or "MixtureDistribution"):
        # Split the params into the mixture weights and the component parameters
        mixture_weights, component_params = tf.split(params, [num_components, event_size * num_components], axis=-1