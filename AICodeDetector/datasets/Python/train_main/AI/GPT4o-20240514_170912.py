

              seq_lengths=None, input_initial_h=None, name='cudnn_gru', reuse=False):
    with tf.variable_scope(name, reuse=reuse):
        # Create initial hidden state
        if input_initial_h is not None:
            initial_h = input_initial_h
        elif trainable_initial_states:
            initial_h = tf.get_variable('initial_h', shape=[n_layers, units.shape[0],