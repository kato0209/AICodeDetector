
  def _make(dist_fn, args):
    if args is None:
      return lambda *_: dist_fn
    if not args:
      return lambda *_: dist_fn()
    def _fn(*xs):
      kwargs = dict(zip(args, reversed(xs[-len(args):])))
      kwargs.pop('_', None)
      return dist_fn(**kwargs)
    return _fn
  named_makers = _convert_to_dict(named_makers)
  g = {k: (None if distribution_util.is_distribution_instance(v)
           else joint_distribution_sequential._get_required_args(v))  # pylint: disable=protected-access
       for k, v in named_makers.items()}
  g = _best_order(g)
  dist_fn_name, dist_fn_args = zip(*g)
  dist_fn_args = tuple(None if a is None else tuple(a) for a