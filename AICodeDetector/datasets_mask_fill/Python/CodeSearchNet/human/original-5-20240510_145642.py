
  @functools.wraps(attr)
  def func(a, *args):
    return attr(a.value, *args)
  return func