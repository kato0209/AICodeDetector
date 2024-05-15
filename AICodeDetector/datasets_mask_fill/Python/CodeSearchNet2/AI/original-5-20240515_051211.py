
    with tf.name_scope(name, "Distribution", [params, event_size]):
      params = tf.convert_to_tensor(params, name="params")
      event_size = tf.convert_to_tensor(event_size, name="event_size")
      event_size.shape.assert_has_rank(0)
      event_size = tf.expand_dims(event_size, 0)
      event_size = tf.tile(event_size, [1, event_size])
      event_size = tf.reshape(event_size, [1,