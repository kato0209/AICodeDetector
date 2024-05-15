
  try:
    return scipy_special.logsumexp(
        input_tensor, axis=_astuple(axis), keepdims=keepdims)
  except NotImplementedError:
    # We offer a non SP version just in case SP isn't installed and this
    # because logsumexp is often used.
    m = _max_mask_non_finite(input_tensor, axis=axis, keepdims=True)
    y = input_tensor - m
    y = np.exp(y, out=y)
    return m + np.log(np.sum(y, axis=_astuple(axis), keepdims=keepdims))