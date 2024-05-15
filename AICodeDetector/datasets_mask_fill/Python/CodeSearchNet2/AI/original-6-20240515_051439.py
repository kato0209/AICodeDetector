
  if not validate_args:
    return
  if not all(
      isinstance(p, distribution_lib.Distribution)
      for p in distributions):
    raise ValueError("All distributions must be from the same distribution.")
  if validate_args:
    distributions = distribution_lib.process_args(
        distribution_lib.NamedDistribution,
        dist_args=validate_args,
        num_samples=None if validate_args else 1)
  if len(distributions)!= len(distributions[0].event_shape):
    raise ValueError("Length of `distributions` must match the number of "
                     "distributions passed in