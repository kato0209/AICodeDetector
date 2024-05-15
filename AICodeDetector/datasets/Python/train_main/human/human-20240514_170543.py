
  state_parts = list(state) if mcmc_util.is_list_like(state) else [state]
  state_parts = [
      tf.convert_to_tensor(value=s, name='current_state') for s in state_parts
  ]
  if state_gradients_are_stopped:
    state_parts = [tf.stop_gradient(x) for x in state_parts]
  target_log_prob, grads_target_log_prob = mcmc_util.maybe_call_fn_and_grads(
      target_log_prob_fn,
      state_parts,
      target_log_prob,
      grads_target_log_prob)
  step_sizes = (list(step_size) if mcmc_util.is_list_like(step_size)
                else [step_size])
  step_sizes = [
      tf.convert_to_tensor(
          value=s, name='step_size', dtype=target_log_prob.dtype)
      for s in step_sizes
  ]
  if len(step_sizes) ==