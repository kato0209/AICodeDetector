
    with tf.variable_scope(scope):
        u = tf.concat([tf.tile(tf.expand_dims(state, axis=1), [1, tf.shape(inputs)[1], 1]), inputs], axis=2)
        logits = tf.layers.dense(tf.layers.dense(u, att_size, activation=tf.nn.tanh), 1, use_bias=False)
        logits = softmax_mask(tf.squeeze(logits, [2]), mask)
        att_weights = tf.expand_dims(tf.nn.softmax(logits), axis=2)
        res = tf.reduce_sum(att_weights * inputs, axis=1)
        return res, logits