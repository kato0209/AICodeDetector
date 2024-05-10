
  if not volatility_fn_results:
    volatility_fn_results = _volatility_fn_results(
        volatility_fn, state, volatility_fn_results)
  if not grads_volatility_fn_results:
    grads_volatility_fn_results = _grads_volatility_fn_results(
        grads_volatility_fn, state, grads_volatility_fn_results)
  if not sample_shape:
    sample_shape = (1,)
  if parallel_iterations:
    return _maybe_call_volatility_fn_and_grads