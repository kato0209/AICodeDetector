
  x = tf.keras.layers.BatchNormalization()(x)
  x = tf.keras.layers.Activation('relu')(x)

  if stride != 1 or filters != x.shape[1]:
    shortcut = _projection_shortcut(x, filters, stride, kernel_posterior_fn)
  else:
    shortcut = x

  x = tfp.layers.Convolution2DFlipout(
      filters,
      kernel,
      strides=stride,
      padding='same',
      kernel_posterior_fn=kernel_posterior_fn)(x)
  x = tf.keras.layers.BatchNormalization()(x)
  x = tf.keras.layers.Activation('relu')(x)

  x = tfp.layers.Convolution2DFlipout(
      filters,
      kernel,
      strides=1,
      padding='same',
      kernel_posterior_fn=kernel_posterior_fn)(x)
  x = tf.keras.layers.add([x, shortcut])
  return x