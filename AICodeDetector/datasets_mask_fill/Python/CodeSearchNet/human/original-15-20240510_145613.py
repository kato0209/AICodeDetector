
  optimizer = tf.compat.v1.train.AdamOptimizer(
      0.1) if optimizer is None else optimizer

  def train_loop_body(step):
    train_op = optimizer.minimize(
        build_loss_fn if tf.executing_eagerly() else build_loss_fn())
    return tf.tuple(tensors=[tf.add(step, 1)], control_inputs=[train_op])

  minimize_op = tf.compat.v1.while_loop(
      cond=lambda step: step < num_steps,
      body=train_loop_body,
      loop_vars=[tf.constant(0)],
      return_same_structure=True)[0]  # Always return a single op.
  return minimize_op