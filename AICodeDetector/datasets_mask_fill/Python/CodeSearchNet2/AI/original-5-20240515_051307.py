
  def _operator_wrapper(self, *args, **kwargs):
    # pylint: disable=protected-access
    if self._in_graph_mode:
      return self._graph._get_function(attr)(*args, **kwargs)
    else:
      return self._graph._get_operation(attr)(*args, **kwargs)

  if attr in self._available_ops:
    return self._available_ops[attr]
  else:
    raise LookupError(
        "Inaccessible Tensor with name %s in %s, which is not "
        "available." % (attr, self))


class