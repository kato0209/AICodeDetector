
  out = tfp.layers.Convolution2DFlipout(
      filters,
      kernel,
      padding='same',
      kernel_posterior_fn=kernel_posterior_fn)(x)
  out = tf.keras.layers.BatchNormalization()(out)
  out = tf.keras.layers.Activation('relu')(out)

  out = tfp.layers.Convolution2DFlipout(
      filters,
      kernel,
      padding='same',
      kernel_posterior_fn=kernel_posterior_fn)(out)
  out = tf.keras.layers.BatchNormalization()(out)
  out = tf.keras.layers.Activation('relu')(out)

  out = tf.keras.layers.MaxPooling2D(
      pool_size=(2, 2), strides=stride)(out)
  return out