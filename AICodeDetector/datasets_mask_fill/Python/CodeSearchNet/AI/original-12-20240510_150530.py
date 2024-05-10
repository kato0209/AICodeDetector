
  x = conv2d_fixed_padding(
      x,
      filters,
      kernel,
      stride,
      padding='VALID',
      kernel_posterior_fn=kernel_posterior_fn)
  x = conv2d_fixed_padding(
      x,
      filters,
      kernel,
      stride,
      padding='VALID',
      kernel_posterior_fn=kernel_posterior_fn)
  x = conv2d_fixed_padding(
      x,
      filters,
      kernel,
      stride,
      padding='VALID',
      kernel_posterior_fn=kernel_posterior_fn)
  x = conv2