

    """Run an optimizer within the graph to minimize a loss function."""
    if optimizer is None:
        optimizer = tf.optimizers.Adam()

    # Build the loss function
    loss = build_loss_fn()

    # Get the trainable variables
    trainable_variables = tf.compat.v1.trainable_variables()

    # Create the training operation
    train_op = optimizer.minimize(loss, var_list=trainable_variables)

    # Initialize variables
    init_op = tf.compat.v1.global_variables_initializer()

