
    with tf.variable_scope(name, reuse=reuse):
        gru = tf.contrib.cudnn_rnn.CudnnGRU(num_layers=n_layers,
                                            num_units=n_hidden)

        if trainable_initial_states:
            init_h = tf.get_variable('init_h', [n_layers, 1, n_hidden])
            init_h = tf.tile(init_h, (1, tf.shape(units)[0], 1))
        else:
            init_h = tf.zeros([n_layers, tf.shape(units)[0], n_hidden])

