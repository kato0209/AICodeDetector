
    # Note: we take `extra_kwargs` as a dict rather than `**extra_kwargs`
    # because it is possible the user provided extra kwargs would itself
    # have `fn`, `event_shape_list`, `static_event_shape_list` and/or
    # `extra_kwargs` as keys.
    with tf.control_dependencies(self._runtime_assertions):
      if event_shape_list is None:
        event_shape_list = [self._event_shape_tensor()]
      if static_event_shape_list is None:
        static_event_shape_list = [self.event_shape]
      new_shape = tf.concat(
          [self._batch_shape_unexpanded] + event_shape_list, axis=0)
      result = tf.reshape(fn(**extra_kwargs) if extra_kwargs else fn(),
      