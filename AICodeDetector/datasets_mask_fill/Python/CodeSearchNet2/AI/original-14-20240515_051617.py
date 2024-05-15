
    # TODO(b/110122868): Remove this function once we switch to using the C API.
    # pylint: disable=protected-access
    # Note that we run this function during the wrap_function for the graph,
    # so we manually remove the 'graph' argument.
    wrapped_func = wrap_function.wrap_function(func, graph)
    # pylint: enable=protected-access
    return wrapped_func.graph._original_func

  # TODO(b/110122868): Remove this function once we switch to using the C API.
  # pylint: disable=protected-access