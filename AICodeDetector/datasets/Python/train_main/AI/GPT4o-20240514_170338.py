
                  volatility_fn,
                  state,
                  step_size,
                  target_log_prob=None,
                  grads_target_log_prob=None,
                  volatility=None,
                  grads_volatility_fn=None,
                  diffusion_drift=None,
                  parallel_iterations=10):
  """Helper which processes input args to meet list-like assumptions."""
  state = list(state) if isinstance(state, (list, tuple)) else [state]
  step_size = list(step_size) if isinstance(step_size, (list, tuple)) else [step_size]

  if target_log_prob is None or grads_target_log_prob is None