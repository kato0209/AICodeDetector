probs`.
    validate_args: Python `bool`, default `False`. When `True` distribution
      parameters are checked for validity despite possibly degrading runtime
      performance. When `False` invalid inputs may silently render incorrect
      outputs.
    name: Python `str` name prefixed to Ops created by this class.

  Returns:
    grid: Shape `[B1,..., Bb, num_samples]`. The sample points of the grid.
    probs: Shape `[B1,..., Bb, num_samples]`. The corresponding (possibly
      normalized) weight.

  Raises:
    ValueError: if `quadrature_