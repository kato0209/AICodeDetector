

    """Gets a Tensor of type `dtype`, 0 if `tol` is None, validation optional."""
    if tol is None:
        return tf.constant(0, dtype=dtype)
    tol = tf.convert_to_tensor(tol, dtype=dtype)
    if validate_args:
        tol = tf.debugging.assert_non_negative(tol)
    return tol
