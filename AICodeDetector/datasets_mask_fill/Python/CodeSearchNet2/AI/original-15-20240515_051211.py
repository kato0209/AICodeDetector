
    with tf.name_scope(name or 'Distribution'):
      params = tf.convert_to_tensor(params, name='params')
      if validate_args:
        params = tf.convert_to_tensor(params, name='params')
      if num_components is None:
        num_components = params.get_shape().as_list()[-1]
      if event_shape is None:
        event_shape = params.get_shape().as_list()[-1]
      if validate_args:
        event_shape = tf.convert_to_tensor(event_shape, name='