
    with tf.variable_scope(scope):
        BS, ML, MH = tf.unstack(tf.shape(memory))
        memory_do = tf.nn.dropout(memory, keep_prob=keep_prob, noise_shape=[BS, 1, MH])
        logits = tf.layers.dense(tf.layers.dense(memory_do, att_size, activation=tf.nn.tanh), 1, use_bias=False)
        logits = softmax_mask(tf.squeeze(logits, [2]), mask)
        att_weights = tf.expand_dims(tf.nn.softmax(logits), axis=2)
        res = tf.reduce_sum(att_weights * memory, axis=1)
        return res