
    if event_shape and all(shape is None for shape in event_shape):
      raise ValueError("event_shape must be specified")
    if validate_args and any(shape is None for shape in params):
      raise ValueError("params must be specified")
    if name is None:
      name = "Distribution"
    with ops.name_scope(name, values=[
        params,
        ops.convert_to_tensor(
            _maybe_validate_shape_dtype(shape),
            name="parameters")
    ]):
      loc = distribution_util.get_distribution_strategy(
        