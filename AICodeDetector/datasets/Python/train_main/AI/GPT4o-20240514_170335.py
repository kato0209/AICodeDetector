

                                        state,
                                        volatility_fn_results=None,
                                        grads_volatility_fn=None,
                                        sample_shape=None,
                                        parallel_iterations=10):
  """Helper which computes `volatility_fn` results and grads, if needed."""
  if volatility_fn_results is None:
    with tf.GradientTape() as tape:
      tape.watch(state)
      volatility_fn_results = volatility_fn(state)
    grads_volatility_fn = tape.gradient(volatility_fn_results, state)
  return volatility_fn_results, grads_volatility_fn
