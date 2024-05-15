
    """Constructs function encapsulated in the graph."""
        with graph.as_default():
            return func(*args, **kwargs)
    return wrapped_func
