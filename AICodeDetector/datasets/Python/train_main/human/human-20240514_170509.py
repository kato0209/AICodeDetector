
  # We use "PrettyDict" because collections.OrderedDict repr/str has the word
  # "OrderedDict" in it. We only want to print "OrderedDict" if in fact the
  # input really is an OrderedDict.
  if isinstance(x, dict):
    return _PrettyDict({
        k: _recursively_replace_dict_for_pretty_dict(v)
        for k, v in x.items()})
  if (isinstance(x, collections.Sequence) and
      not isinstance(x, six.string_types)):
    args = (_recursively_replace_dict_for_pretty_dict(x_) for x_ in x)
    is_named_tuple = (isinstance(x, tuple) and
                      hasattr(x, "_asdict") and
         