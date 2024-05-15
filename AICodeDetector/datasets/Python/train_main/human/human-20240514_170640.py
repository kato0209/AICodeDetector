
  if tol is None:
    return tf.convert_to_tensor(value=0, dtype=dtype)

  tol = tf.convert_to_tensor(value=tol, dtype=dtype)
  if validate_args:
    tol = distribution_util.with_dependencies([
        assert_util.assert_non_negative(
            tol, message="Argument 'tol' must be non-negative")
    ], tol)
  return tol