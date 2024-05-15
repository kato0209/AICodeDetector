
  with tf.name_scope(name or "process_quadrature_grid_and_probs"):
    if quadrature_grid_and_probs is None:
      grid, probs = np.polynomial.hermite.hermgauss(deg=8)
      grid = grid.astype(dtype_util.as_numpy_dtype(dtype))
      probs = probs.astype(dtype_util.as_numpy_dtype(dtype))
      probs /= np.linalg.norm(probs, ord=1, keepdims=True)
      grid = tf.convert_to_tensor(value=grid, name="grid", dtype=dtype)
      probs = tf.convert_to_tensor(value=probs, name="probs", dtype=dtype)
      return grid, probs

    grid, probs = tuple(quadrature_grid_and_probs)
    grid = tf.convert_to_tensor(value=grid, name="grid", dtype=dtype)
    probs = tf.convert_to_tensor(
        value=probs, name="unnormalized_probs", dtype=dtype)
    probs /= tf.norm(tensor=probs, ord=1, axis=-1, keepdims=True, name="probs")

    def _static_event_size(x):
      