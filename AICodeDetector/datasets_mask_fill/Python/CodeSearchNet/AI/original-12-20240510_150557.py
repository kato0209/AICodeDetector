
  if not isinstance(params_event_ndims, int):
    params_event_ndims = ops.convert_to_tensor(params_event_ndims, name="params_event_ndims")
    if params_event_ndims.shape.ndims!= 0:
      raise ValueError("params_event_ndims must be a scalar")
    if params_event_ndims.shape.ndims == 0:
      params_event_ndims = array_ops.shape(dist.batch_shape_tensor())[0]

    # We do not support `None` in the params_event_ndims.
    if params_