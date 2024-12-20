
  state_parts = list(state) if mcmc_util.is_list_like(state) else [state]
  needs_volatility_fn_gradients = grads_volatility_fn is None

  # Convert `volatility_fn_results` to a list
  if volatility_fn_results is None:
    volatility_fn_results = volatility_fn(*state_parts)

  volatility_fn_results = (list(volatility_fn_results)
                           if mcmc_util.is_list_like(volatility_fn_results)
                           else [volatility_fn_results])
  if len(volatility_fn_results) == 1:
    volatility_fn_results *= len(state_parts)
  if len(state_parts) != len(volatility_fn_results):
    raise ValueError('`volatility_fn` should return a tensor or a list '
      