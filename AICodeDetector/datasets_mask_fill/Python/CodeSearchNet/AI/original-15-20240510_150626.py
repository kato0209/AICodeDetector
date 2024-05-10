
  def _prior_fn(unused_theta, unused_log_prob_fn, unused_sample_fn,
                observation_and_action_log_prob_fn,
                seed=None):
    del unused_theta, unused_log_prob_fn, unused_sample_fn, observation_and_action_log_prob_fn
    return _prior_fn_with_log_prob_fn(
        num_topics=num_topics,
        initial_value=initial_value,
        seed=seed)
  return _prior_fn


def make_multivariate_normal_