

  # If the current season has just ended, increase the variance of its effect
  # following drift_scale. (the just-ended seasonal effect will always be the
  # bottom element of the vector). Otherwise, do nothing.
  drift_scale_diag = tf.stack(
      [tf.zeros_like(drift_scale)] * (num_seasons - 1) + [drift_scale],
      axis=-1)
  def seasonal_transition_noise(t):
    noise_scale_diag = dist_util.pick_scalar_condition(
        is_last_day_of_season(t),
        drift_scale_diag,
        tf.zeros_like(drift_scale_diag))
    return tfd.MultivariateNormalDiag(
        loc=tf.zeros(num_seasons, dtype=drift_scale.dtype),
        scale_diag=noise_scale_diag)
  return seasonal_transition_noise