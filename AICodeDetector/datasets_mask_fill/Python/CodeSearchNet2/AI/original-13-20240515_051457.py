 of `dense_vector`.
    validate_args: Python `bool`, default `False`. When `True` distribution
      parameters are checked for validity despite possibly degrading runtime
      performance. When `False` invalid inputs may silently render incorrect
      outputs.
    name: Python `str` name prefixed to Ops created by this class.
    **kwargs: For backwards compatibility.

  Returns:
    batched_matmul: A (batch of) matrix-matrix `Tensor` representing the
      (non-batch) matmul of the (non-batch) matrix `Tensor`.

  Raises:
    ValueError:  If `