
  transition_noise = tf.random.normal(
      shape=[num_seasons, 1], stddev=drift_scale, dtype=tf.float32)
  transition_noise = tf.where(
      tf.greater(transition_noise, 0.0),
      transition_noise,
      tf.zeros_like(transition_noise),
      name='transition_noise')
  transition_noise = tf.where(
      tf.greater(transition_noise, 1.0),
      transition_noise,
      tf.zeros_like(transition_noise),
      name='transition_noise')
  transition_