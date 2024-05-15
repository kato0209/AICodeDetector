
    """Helper to merge which handles merging one value."""
    if use_equals:
        return new if new != old else old
    else:
        return new if new is not None else old
