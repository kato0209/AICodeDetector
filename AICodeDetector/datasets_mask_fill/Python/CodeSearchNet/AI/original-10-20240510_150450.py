
    with tf.name_scope(name or 'Distribution'):
      params = tf.convert_to_tensor(params, name='params')
      event_shape = tf.convert_to_tensor(event_shape, name='event_shape')
      event_shape = tf.convert_to_tensor(event_shape, name='event_shape')
      if validate_args:
        event_shape = tf.convert_to_tensor(event_shape, name='event_shape')
        event_shape = tf.convert_to_tensor(event_shape, name='event_shape')