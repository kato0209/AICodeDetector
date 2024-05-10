
  forward_fn_name = 'forward_transform_fn'
  if bijector.name:
    forward_fn_name = bijector.name + '/forward_transform_fn'
  return forward_fn_lib.Lambda(
      forward_fn_name, bijector.forward_name, bijector.forward_params,
      bijector.forward_inverse_fn, bijector.forward_inverse_params,
      bijector.forward_inverse_inverse_log_det_jacobian,
      bijector.forward_inverse_log_det_jacobian_bijector,
      validate_args=