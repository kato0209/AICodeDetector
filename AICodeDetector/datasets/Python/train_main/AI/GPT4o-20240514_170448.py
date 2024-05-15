

                                      dtype,
                                      validate_args,
                                      name=None):
  with tf.name_scope(name or 'process_quadrature_grid_and_probs'):
    if quadrature_grid_and_probs is None:
      grid, probs = np.polynomial.hermite.hermgauss(deg=8)
      grid = tf.convert_to_tensor(grid, dtype=dtype)
      probs = tf.convert_to_tensor(probs, dtype=dtype)
    else:
      grid, probs = quadrature_grid_and_probs
      grid =