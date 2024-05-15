
    """Sample shape of random variable as a 1-D `Tensor`.

    Args:
      name: name to give to the op

    Returns:
      sample_shape: `Tensor`.
    """
    with tf.name_scope(name):
        return tf.convert_to_tensor(self.sample_shape, dtype=tf.int32, name="sample_shape")
