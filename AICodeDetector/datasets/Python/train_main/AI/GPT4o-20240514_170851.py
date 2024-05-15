

    with tf.variable_scope(scope):
        # Linear transformation of the state
        state_proj = tf.layers.dense(state, att_size, activation=tf.tanh, name="state_proj")
        
        # Linear transformation of the inputs
        inputs_proj = tf.layers.dense(inputs, att_size, activation=tf.tanh, name="inputs_proj")
        
        # Compute the attention scores
        scores = tf.reduce_sum(tf.tanh(state_proj + inputs_proj), axis=-1)
        
        # Apply mask to the scores