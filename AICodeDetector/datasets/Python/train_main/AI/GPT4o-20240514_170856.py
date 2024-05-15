

    """Get summary ops for the magnitude of gradient updates."""
    summaries = []
    for grad, var in grads:
        if grad is not None:
            grad_update = opt.apply_gradients([(grad, var)], global_step=tf.train.get_or_create_global_step())
            with tf.control_dependencies([grad_update]):
                grad_norm = tf.norm(grad)
                update_norm = tf.norm(lr * grad)
                summaries.append(tf.summary.scalar(f'{var.op.name}/grad_norm', grad_norm))
                summaries.append(tf.summary.scalar(f'{