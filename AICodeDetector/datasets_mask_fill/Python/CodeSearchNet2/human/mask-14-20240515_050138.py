
  state_parts = list(state) if mcmc_util.is_list_like(state) else [state]
  state_parts = [
      tf.convert_to_tensor(value=s, name='current_state') for s in state_parts
  ]

  target_log_prob = _maybe_call_fn(
      target_log_prob_fn,
      state_parts,
      target_log_prob,
      description)
  step_sizes = (list(step_size) if mcmc_util.is_list_like(step_size)
                else [step_size])
  step_sizes = [
      tf.convert_to_tensor(
          value=s, name='step_size', dtype=target_log_prob.dtype)
      for s in step_sizes
  ]
  if len(step_sizes) == 1:
    step_sizes *= len(state_parts)
  if len(state_parts) != len(step_sizes):
  