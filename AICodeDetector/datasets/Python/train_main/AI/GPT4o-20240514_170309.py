

    """Replicate the input tensor n times along a new (major) dimension."""
    return np.tile(tensor, (n,) + (1,) * tensor.ndim)
