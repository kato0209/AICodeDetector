
    event_dim = (
        tf.compat.dimension_value(self.event_shape[0]) or
        self._event_shape_tensor()[0])
    basis = tf.concat([[1.], tf.zeros([event_dim - 1], dtype=self.dtype)],
                      axis=0),
    u = tf.nn.l2_normalize(basis - self.mean_direction, axis=-1)
    return samples - 2 * tf.reduce_sum(
        input_tensor=samples * u, axis=-1, keepdims=True) * u