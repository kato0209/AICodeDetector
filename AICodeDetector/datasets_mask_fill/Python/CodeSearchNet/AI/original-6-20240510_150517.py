
  with tf.variable_scope('visualize_qualitative_analysis'):
    # Create the input placeholder.
    inputs = tf.placeholder(tf.float32, [None, samples, length])

    # Create the model.
    model = model(inputs)

    # Create the loss.
    loss = tf.reduce_mean(model.losses)

    # Create the optimizer.
    optimizer = tf.train.AdamOptimizer(learning_rate=0.001)

    # Create the train_op.
    train_op = optimizer.minimize(loss)

    # Create the saver.
    saver = tf