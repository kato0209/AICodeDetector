
  state_parts = list(state) if mcmc_util.is_list_like(state) else [state]

  [
      target_log_prob,
      grads_target_log_prob,
  ] = mcmc_util.maybe_call_fn_and_grads(
      target_log_prob_fn,
      state_parts,
      target_log_prob,
      grads_target_log_prob)
  [
      volatility_parts,
      grads_volatility,
  ] = _maybe_call_volatility_fn_and_grads(
      volatility_fn,
      state_parts,
      volatility,
      grads_volatility_fn,
      distribution_util.prefer_static_shape(target_log_prob),
      parallel_iterations)

  step_sizes = (list(step_size) if mcmc_util.is_list_like(step_size)
                else [step_size])
