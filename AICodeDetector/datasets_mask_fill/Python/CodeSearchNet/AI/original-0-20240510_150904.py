
    if dropout > 0.0:
        inputs = tf.nn.dropout(inputs, 1.0 - dropout)
    return inputs


def Conv2D(inputs, kernel_size, filters, strides, padding='SAME',
           data_format='channels_last', activation=tf.nn.relu,
           kernel_initializer=tf.contrib.layers.xavier_initializer(),
           bias_initializer=tf.zeros_initializer(),
           kernel_regularizer=None, bias_regularizer=None,
           activity_regularizer=None, kernel_constraint=None,
           bias_constraint=None, **kwargs