

  num_schools = 8
  treatment_effects = tf.constant(
      [28, 8, -3, 7, -1, 1, 18, 12],
      dtype=np.float32,
      name='treatment_effects')
  treatment_stddevs = tf.constant(
      [15, 10, 16, 11, 9, 11, 10, 18],
      dtype=np.float32,
      name='treatment_stddevs')

  def unnormalized_posterior_log_prob(
      avg_effect, avg_stddev, school_effects_standard):
    