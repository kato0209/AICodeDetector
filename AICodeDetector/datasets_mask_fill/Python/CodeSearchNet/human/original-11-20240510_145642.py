
  if hasattr(f, "_func"):  # functions returned by tf.make_template
    f = f._func  # pylint: disable=protected-access

  try:  # getargspec was deprecated in Python 3.6
    argspec = inspect.getfullargspec(f)
  except AttributeError:
    argspec = inspect.getargspec(f)

  fkwargs = {k: v for k, v in six.iteritems(src_kwargs) if k in argspec.args}
  return fkwargs