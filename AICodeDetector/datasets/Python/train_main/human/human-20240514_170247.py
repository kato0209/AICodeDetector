

  if not tf.executing_eagerly():
    tf.compat.v1.reset_default_graph()

  # Build a static, pretend dataset.
  count_data = tf.cast(
      tf.concat(
          [tfd.Poisson(rate=15.).sample(43),
           tfd.Poisson(rate=25.).sample(31)],
          axis=0),
      dtype=tf.float32)
  if tf.executing_eagerly():
    count_data = count_data.numpy()
  else:
    with tf.compat.v1.Session():
      count_data = count_data.eval()

  # Define a closure over our joint_log_prob.
  def unnormalized_log_posterior(lambda1, lambda2, tau):
    return text_messages_joint_log_prob(count_data, lambda1, lambda2, tau)

  if tf.executing_eagerly():
    sample_chain = tf.function(tfp.mcmc.sample_chain)
  else:
    sample_chain = tfp.mcmc.sample_chain

  # Initialize