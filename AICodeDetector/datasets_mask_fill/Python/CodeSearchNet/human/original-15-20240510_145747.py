
  def _softplus_inverse(x):
    return np.log(np.expm1(x))

  logit_concentration = tf.compat.v1.get_variable(
      "logit_concentration",
      shape=[1, num_topics],
      initializer=tf.compat.v1.initializers.constant(
          _softplus_inverse(initial_value)))
  concentration = _clip_dirichlet_parameters(
      tf.nn.softplus(logit_concentration))

  def prior():
    return tfd.Dirichlet(concentration=concentration,
                         name="topics_prior")

  prior_variables = [logit_concentration]

  return prior, prior_variables