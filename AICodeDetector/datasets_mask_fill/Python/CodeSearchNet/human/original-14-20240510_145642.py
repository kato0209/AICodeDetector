
  mid_momentum = [
      m + 0.5 * step * g for m, step, g in
      zip(current_momentum, step_size, current_grads_target_log_prob)]
  next_state = [
      s + step * m for s, step, m in
      zip(current_state, step_size, mid_momentum)]
  next_target_log_prob, next_grads_target_log_prob = value_and_gradients_fn(
      *next_state)
  next_momentum = [
      m + 0.5 * step * g for m, step, g in
      zip(mid_momentum, step_size, next_grads_target_log_prob)]
  return [
      next_state,
      next_target_log_prob,
      next_grads_target_log_prob,
      next_momentum,
  ]