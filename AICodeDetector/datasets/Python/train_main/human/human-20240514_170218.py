
  state_parts = list(state) if mcmc_util.is_list_like(state) else [state]
  state_parts = [tf.convert_to_tensor(s, name='current_state')
                 for s in state_parts]

  log_likelihood = _maybe_call_fn(
      log_likelihood_fn,
      state_parts,
      log_likelihood,
      description)
  return [state_parts, log_likelihood]