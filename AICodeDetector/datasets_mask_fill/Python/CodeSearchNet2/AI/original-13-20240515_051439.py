 = D_f[q, p]`.

  Warning: this function makes non-log-space calculations and may therefore be
  numerically unstable for `|logu| >> 0`.

  Args:
    logu: `float`-like `Tensor` representing `log(u)` from above.
    name: Python `str` name prefixed to Ops created by this function.
      Default value: `None` (i.e., 'logu').

  Returns:
    triangular: `Tensor` of shape `[..., M, M]`.

  Raises:
    ValueError: if `logu` is not in