
    """Computes graph and static `sample_shape`."""
    if isinstance(x, tf.Tensor):
        return tf.shape(x)
    elif isinstance(x, np.ndarray):
        return x.shape
    else:
        raise TypeError("Input must be a TensorFlow tensor or a NumPy array.")
