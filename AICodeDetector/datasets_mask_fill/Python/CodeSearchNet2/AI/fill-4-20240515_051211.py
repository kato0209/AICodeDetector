
  if use_exact_kl:
    kl_fn = tfd.kl_divergence_fn
    kl_fn = tfd.kl_divergence_fn_with_checks(
        distribution_b,
        test_points_reduce_axis=test_points_reduce_axis,
        test_points_fn=test_points_fn,
        weight=weight)
  else:
    kl_fn = tfd.kl_divergence_fn_with_checks(
        distribution_b,
        test_points_reduce_axis=test_points_reduce_axis,
        test_points_fn