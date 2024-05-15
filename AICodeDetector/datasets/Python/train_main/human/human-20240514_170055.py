
    with tf.compat.v1.name_scope(name, 'IndependentBernoulli',
                                 [params, event_shape]):
      params = tf.convert_to_tensor(value=params, name='params')
      event_shape = dist_util.expand_to_vector(
          tf.convert_to_tensor(
              value=event_shape, name='event_shape', dtype_hint=tf.int32),
          tensor_name='event_shape')
      new_shape = tf.concat([
          tf.shape(input=params)[:-1],
          event_shape,
      ],