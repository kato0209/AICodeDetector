
    """Constructs function encapsulated in the graph and the session."""
        with graph.as_default():
            with session.as_default():
                return func(*args, **kwargs)
    return wrapper
