
                  log_likelihood=None, description='log_likelihood'):
  """Processes input args to meet list-like assumptions."""
  if log_likelihood is None:
    log_likelihood = [log_likelihood_fn(s) for s in state]
  elif not isinstance(log_likelihood, (list, tuple)):
    raise TypeError(f'{description} must be a list or tuple.')
  return log_likelihood
