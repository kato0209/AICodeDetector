
  if not mcmc_util.is_list_like(bijector):
    bijector = [bijector]

  def fn(transformed_state_parts):
    return [b.forward(sp) for b, sp in zip(bijector, transformed_state_parts)]

  return fn