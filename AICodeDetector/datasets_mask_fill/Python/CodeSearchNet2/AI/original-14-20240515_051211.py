
    with tf.name_scope(name, "params_size", values=[num_components]):
      event_shape = tf.convert_to_tensor(event_shape, name="event_shape")
      event_shape = tf.convert_to_tensor(event_shape, name="event_shape")
      event_shape = tf.reshape(event_shape, [num_components])
      event_shape = tf.transpose(event_shape, [1, 0, 2])
      event_shape = tf.reshape(event_shape, [num_components, -1])
      event