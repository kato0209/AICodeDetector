

    """Checks that input is a `float` matrix."""
    if validate_args:
        if not isinstance(a, np.ndarray):
            raise ValueError("Input must be a numpy array.")
        if not np.issubdtype(a.dtype, np.floating):
            raise ValueError("Input matrix must be of float type.")
    return a
