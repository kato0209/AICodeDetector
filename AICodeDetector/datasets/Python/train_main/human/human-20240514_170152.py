
  # We want to write the following 2 x 2 matrix:
  #  [[1., 1., ],    # level(t+1) = level(t) + slope(t)
  #   [0., ar_coef], # slope(t+1) = ar_coef * slope(t)
  # but it's slightly tricky to properly incorporate the batch shape of
  # autoregressive_coef. E.g., if autoregressive_coef has shape [4,6], we want
  # to return shape [4, 6, 2, 2]. We do this by breaking the matrix into its
  # fixed entries, written explicitly, and then the autoregressive_coef part
  # which we add in after using a mask to broadcast to the correct matrix shape.

  fixed_entries = tf.constant(
      [[1., 1.],
       [0.,