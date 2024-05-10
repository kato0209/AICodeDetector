
  # Note that this function is not differentiable, and is only used in
  # _inverse_hessian_estimate.
  # TODO(b/151145004): Remove this function once we refactor the b/151145004
  # optimizer code.
  if not hasattr(prev_state, "_inv_hessian_estimate"):
    return

  # Compute the inverse hessian using the previous state estimate.
  # Note that this function is not differentiable, and is only used in
  # _inverse_hessian_estimate.
  if not hasattr(next_state, "_inv_hessian_