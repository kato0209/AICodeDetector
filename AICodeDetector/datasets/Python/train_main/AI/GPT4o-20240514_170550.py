

    """Network block for ResNet."""
    conv1 = tfp.layers.Convolution2DFlipout(
        filters, kernel, strides=stride, padding='same',
        kernel_posterior_fn=kernel_posterior_fn)(x)
    conv1 = tf.keras.layers.BatchNormalization()(conv1)
    conv1 = tf.keras.layers.ReLU()(conv1)

    conv2 = tfp.layers.Convolution2DFlipout(
        filters, kernel