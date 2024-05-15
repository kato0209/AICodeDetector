
                  target_log_prob=None, maybe_expand=False,
                  description='target_log_prob'):
  """Processes input args to meet list-like assumptions."""
  if not isinstance(state, (list, tuple)):
    state = [state]
  if not isinstance(step_size, (list, tuple)):
    step_size = [step_size] * len(state)
  if target_log_prob is None:
    target_log_prob = target_log_prob_fn(*state)
  if maybe_expand:
    state = [s[tf.newaxis, ...] for s in state]
