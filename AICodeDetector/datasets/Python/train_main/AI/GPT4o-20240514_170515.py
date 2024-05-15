

    """Check that a shape Tensor is int-type and otherwise sane."""
    if validate_args:
        shape = tf.convert_to_tensor(shape, dtype=tf.int32)
        tf.debugging.assert_type(shape, tf.int32, message="Shape must be an int32 tensor")
        tf.debugging.assert_non_negative(shape, message="Shape values must be non-negative")
    return shape
