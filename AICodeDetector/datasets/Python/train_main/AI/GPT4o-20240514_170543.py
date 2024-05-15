
                  state,
                  step_size,
                  target_log_prob=None,
                  grads_target_log_prob=None,
                  maybe_expand=False,
                  state_gradients_are_stopped=False):
  """Helper which processes input args to meet list-like assumptions."""
  if not isinstance(state, (list, tuple)):
    state = [state]
  if not isinstance(step_size, (list, tuple)):
    step_size = [step_size] * len(state)
  if target_log_prob is None:
    target_log_prob = target_log_prob_fn(*state)
  if grads_target_log_prob is None