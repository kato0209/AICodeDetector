
  if value_and_gradients_fn is None:
    return None
  if current_state is None:
    current_state = value_and_gradients_fn(current_grads_target_log_prob)
  if current_state is None:
    return None
  if current_state.shape.ndims == 0:
    return None
  if current_state.shape.ndims == 1:
    return value_and_gradients_fn(current_state)
  if current_state.shape.ndims == 2:
    return value_and_gradients_fn(current_state, current_grads_