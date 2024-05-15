

    """Learnable Gamma via concentration and scale parameterization."""
    concentration = tf.Variable(
        initial_value=tf.random.uniform(shape, minval=min_concentration, maxval=1.0),
        trainable=True,
        name=name + '_concentration' if name else None
    )
    scale = tf.Variable(
        initial_value=tf.random.uniform(shape, minval=min_scale, maxval=1.0),
        trainable=True,
        name=name +