
    with tf.variable_scope(scope, values=[inputs, att_size]):
        attention_inputs = tf.nn.conv2d(
            inputs,
            state,
            strides=[1, 1, 1, 1],
            padding="VALID",
            name="attention_inputs")
        attention_state = tf.nn.conv2d(
            attention_inputs,
            state,
            strides=[1, 1,