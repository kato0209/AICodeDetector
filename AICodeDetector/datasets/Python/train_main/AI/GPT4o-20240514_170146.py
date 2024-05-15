
    """Checks the validity of a sample."""
    if not isinstance(x, (int, float)):
        raise ValueError("Sample must be an integer or float.")
    if x < 0:
        raise ValueError("Sample must be non-negative.")
