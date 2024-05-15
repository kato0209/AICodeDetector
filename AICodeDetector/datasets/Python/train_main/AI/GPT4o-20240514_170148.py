

    """Return a list (preferred) or 1d Tensor from values, if values.ndims < 2."""
    if isinstance(values, tf.Tensor):
        if values.ndim < 2:
            return values
        else:
            raise ValueError("Tensor has more than 1 dimension")
    elif isinstance(values, (list, tuple)):
        return list(values)
    else:
        raise TypeError("Input must be a Tensor, list, or tuple")
