
    with tf.name_scope(name, "params_size"):
      event_size = tf.convert_to_tensor(event_size, name="event_size")
      event_size = tf.reshape(event_size, [1, -1])
      event_size = tf.tile(event_size, [1, num_components])
      event_size = tf.reshape(event_size, [1, -1])
      event_size = tf.tile(event_size, [num_components, 1])
      event_size = tf.reshape(event_size