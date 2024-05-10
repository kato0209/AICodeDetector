
    if event_size is None:
      event_size = array_ops.shape(params)[0]
    if validate_args:
      event_size = np.asarray(event_size, dtype=dtype)
    if not dtype:
      dtype = param_base.dtype
    if name is None:
      name = param_base.name
    return type(params)(
        distribution_util.Uniform(
            low=params.low, high=params.high,
            validate_args=validate_args,
            allow_nan_stats=True,
            name=name),
       