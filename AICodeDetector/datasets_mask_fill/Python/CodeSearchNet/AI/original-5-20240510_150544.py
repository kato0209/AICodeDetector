
  # TODO(b/1414741686): Remove this once we have a better way to handle
  # the case where we have a single target.
  if target_log_prob is None:
    target_log_prob = tf.constant(0.0)

  if volatility_fn is None:
    volatility_fn = tf.constant(0.0)

  if grads_target_log_prob is None:
    grads_target_log_prob = tf.constant(0.0)

  if volatility is None:
    volatility = tf.constant(0.0