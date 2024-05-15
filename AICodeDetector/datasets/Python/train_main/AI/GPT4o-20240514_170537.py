
                          initial_args,
                          val_0,
                          val_c,
                          f_lim,
                          sufficient_decrease_param,
                          curvature_param):
  """Helper function for secant-square step."""
    denom = (grad_c - grad_0)
    if denom == 0:
      step = step_c
    else:
      step = step_c - grad_c * (step_c - step_0) / denom

    new_args