

    """Assert x is a non-negative tensor, and optionally of integers."""
    with tf.name_scope(name):
        x = tf.convert_to_tensor(x, name="x")
        if not x.dtype.is_integer:
            raise TypeError(f"Expected integer type for {name}, but got {x.dtype}")
        if tf.reduce_any(x < 0):
            raise ValueError(f"Tensor {name} contains negative values")
    return x
