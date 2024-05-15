
  def _fn(self):
    if any(self._dist_fn_args):  # pylint: disable=protected-access
      raise ValueError(
          'Can only compute ' + attr + ' when all distributions are '
          'independent; {}'.format(self.model))
    return self._unflatten(getattr(d(), attr)() for d in self._dist_fn_wrapped)  # pylint: disable=protected-access
  return _fn