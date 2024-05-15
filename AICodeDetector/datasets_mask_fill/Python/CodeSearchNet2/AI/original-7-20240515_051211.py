
    dtype = dtype or params.dtype
    if dtype not in [dtypes.half, dtypes.float32, dtypes.float64]:
      raise TypeError("Invalid dtype %r" % dtype)
    if params.dtype.is_integer:
      dtype = _assert_integer_form(dtype)
    else:
      dtype = _assert_float_form(dtype)

    distribution = distribution_util.make_template(
        name, params=params, dtype=dtype, validate_args=validate_args)
    self._distribution = distribution
    self._parameters = parameters or {}
    self._graph_parents =