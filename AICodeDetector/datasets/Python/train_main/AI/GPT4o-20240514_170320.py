
              current_state,
              current_grads_target_log_prob,
              current_momentum,
              step_size):
  """Runs one step of leapfrog integration."""
  # Half step update for momentum
  new_momentum = [m + 0.5 * step_size * g for m, g in zip(current_momentum, current_grads_target_log_prob)]

  # Full step update for position
  new_state = [s + step_size * m for s, m in zip(current_state, new_momentum)]

  # Compute new gradients
  new_target