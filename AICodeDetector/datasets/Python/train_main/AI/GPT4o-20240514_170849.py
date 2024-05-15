

    with tf.variable_scope(scope):
        memory_shape = memory.get_shape().as_list()
        query = tf.get_variable("query", [att_size], dtype=tf.float32)
        
        keys = tf.layers.dense(memory, att_size, use_bias=False, name="keys")
        logits = tf.reduce_sum(keys * query, axis=-1)
        
        if mask is not None:
            logits = tf.where(mask, logits, tf.fill(tf.shape(logits), float('-inf