
    with self._name_scope(name):
      # Linspace only takes scalars, so we'll add in the offset afterwards.
      seq = tf.linspace(
          tf.constant(0., dtype=self.dtype), 0.5 - 0.5 * p, tf.cast(
              p, tf.int32))
      return seq + tf.expand_dims(a, [-1])