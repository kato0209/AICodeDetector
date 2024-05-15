
    # Note: we take `extra_kwargs` as a dict rather than `**extra_kwargs`
    # because it is possible the user provided extra kwargs would itself
    # have `fn` and/or `x` as a key.
    with tf.control_dependencies(self._runtime_assertions +
                                 self._validate_sample_arg(x)):
      sample_shape, static_sample_shape = self._sample_shape(x)
      old_shape = tf.concat(
          [
              sample_shape,
       