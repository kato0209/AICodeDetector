
  if isinstance(d, (float, int, np.generic, np.ndarray)):
    n = (-1 + np.sqrt(1 + 8 * d)) / 2.
    if float(int(n)) != n:
      raise ValueError("Vector length is not a triangular number.")
    return int(n)
  else:
    with tf.name_scope(name or "vector_size_to_square_matrix_size") as name:
      n = (-1. + tf.sqrt(1 + 8. * tf.cast(d, dtype=tf.float32))) / 2.
      if validate_args:
        with tf.control_dependencies([
            assert_util.assert_equal(
                tf.cast(tf.cast(n, dtype=tf.int32), dtype=tf.float32),
       