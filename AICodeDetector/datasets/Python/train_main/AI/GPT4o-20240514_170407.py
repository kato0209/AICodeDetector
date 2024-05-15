

    """Returns the maximum representable value in this data type."""
    return np.iinfo(dtype).max if np.issubdtype(dtype, np.integer) else np.finfo(dtype).max
