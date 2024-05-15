

    with tf.name_scope(name or "event_size"):
        event_shape = tf.convert_to_tensor(event_shape, dtype=tf.int32, name="event_shape")
        if event_shape.shape.is_fully_defined():
            return event_shape.shape.num_elements()
        else:
            return tf.reduce_prod(event_shape)
