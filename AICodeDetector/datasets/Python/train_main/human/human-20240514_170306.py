
    if isinstance(self._sample_shape, tf.Tensor):
      return tf.TensorShape(tf.get_static_value(self._sample_shape))
    return tf.TensorShape(self._sample_shape)