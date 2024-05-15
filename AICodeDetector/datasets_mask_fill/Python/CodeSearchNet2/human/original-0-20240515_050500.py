
  # center = Max[Log[values]],  with stop-gradient
  # The center hopefully keep the exponentiated term small.  It is canceled
  # from the final result, so putting stop gradient on it will not change the
  # final result.  We put stop gradient on to eliminate unnecessary computation.
  center = tf.stop_gradient(_sample_max(log_values))

  # centered_values = exp{Log[values] - E[Log[values]]}
  centered_values = tf.math.exp(log_values - center)

  # log_mean_of_values = Log[ E[centered_values] ] + center
  #                    = Log[ E[exp{log_values - E[log_values]}] ] + center
  #                  