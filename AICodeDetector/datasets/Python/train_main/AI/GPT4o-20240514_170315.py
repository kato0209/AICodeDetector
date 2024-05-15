

    """Network block for VGG."""
    x = tfp.layers.Convolution2DFlipout(
        filters,
        kernel,
        strides=stride,
        padding='same',
        kernel_posterior_fn=kernel_posterior_fn,
        activation='relu'
    )(x)
    x = tfp.layers.Convolution2DFlipout(
        filters,
        kernel,
        strides=1,
        padding='same',
        kernel_posterior