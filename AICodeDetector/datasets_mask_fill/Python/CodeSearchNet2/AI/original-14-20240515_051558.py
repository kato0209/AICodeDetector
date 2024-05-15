
    with tf.variable_scope(scope, reuse=True):
        # Encoder.
        encoder_outputs = tf.layers.dense(
            memory,
            att_size,
            activation=tf.nn.relu,
            kernel_initializer=tf.random_normal_initializer(stddev=0.01),
            name="encoder_outputs")
        encoder_outputs = tf.layers.dropout(encoder_outputs, keep_prob)

        # Decoder.
        decoder_outputs = tf.layers.dense(
            decoder_outputs,
