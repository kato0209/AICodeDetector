

  predicted_mean = _propagate_mean(filtered_mean,
                                   transition_matrix,
                                   transition_noise)
  predicted_cov = _propagate_cov(filtered_cov,
                                 transition_matrix,
                