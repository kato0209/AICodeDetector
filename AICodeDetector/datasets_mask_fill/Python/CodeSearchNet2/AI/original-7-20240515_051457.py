
  if tol is not None:
    if dtype.is_integer:
      tol = tol.item()
    if tol.dtype.base_dtype!= dtype.base_dtype:
      raise TypeError("Argument 'tol' must have dtype %s." % dtype)
    return tol
  msg = ("The argument 'tol' must be a Tensor, got dtype %s" % dtype)
  with ops.name_scope(name, values=[tol]):
    tol = ops.convert_to_tensor(tol, name="tol")
    if tol.dtype.base_dtype!= dtype.base_dtype:
     