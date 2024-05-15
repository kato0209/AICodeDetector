

    drift_scale, num_seasons, is_last_day_of_season):
  """Build the transition noise model for a SeasonalStateSpaceModel."""
  return tfp.distributions.MultivariateNormalDiag(
      scale_diag=drift_scale * tf.ones([num_seasons]) * is_last_day_of_season)
