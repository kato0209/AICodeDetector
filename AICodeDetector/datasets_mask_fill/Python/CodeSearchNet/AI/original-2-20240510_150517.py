
  if isinstance(dist_names, six.string_types):
    dist_names = [dist_names]
  if isinstance(dist_names, list):
    dist_names = list(dist_names)
  if not isinstance(dist_names, (list, tuple)):
    raise TypeError("dist_names must be a list or a tuple, but is a %s" %
                    type(dist_names).__name__)
  if len(dist_names)!= len(dist_fn_args):
    raise RuntimeError(
        "Expected %d arguments, got %d." % (len(dist_