
  x = conv2d_fixed_padding(x, kernel_size=3, strides=stride,
                           data_format=K.image_data_format(),
                           activation=None,
                           use_bias=False,
                           kernel_initializer=kernel_posterior_fn(kernel))
  x = conv2d_fixed_padding(x, kernel_size=3, strides=1,
       