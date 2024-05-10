
  assertions = []

  if not _is_iterable(distributions) or not distributions:
    raise ValueError('`distributions` must be a list of one or more '
                     'distributions.')

  if dtype_override is None:
    dts = [
        dtype_util.base_dtype(d.dtype)
        for d in distributions
        if d.dtype is not None
    ]
    if dts[1:] != dts[:-1]:
      raise TypeError('Distributions must have same dtype; found: {}.'.format(
          set(dtype_util.name(dt) for dt in dts)))

 