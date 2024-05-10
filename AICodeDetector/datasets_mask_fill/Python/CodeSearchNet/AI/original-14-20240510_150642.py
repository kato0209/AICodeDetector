ar_function(logu=logu, u=u)
       = 0.5 kl_forward + 0.5 kl_reverse + 0.5 kl_reverse + 0.5 kl_forward
       = symmetrized_csiszar_function(logu=logu, u=u)

  Args:
    logu: `float`-like `Tensor` representing `log(u)` from above.
    name: Python `str` name prefixed to Ops created by this function.
      Default value: `None` (i.e., `'kl_forward'`).

  Returns