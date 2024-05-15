
    """Computes `rank` given a `Tensor`'s `shape`."""
    if tensorshape is not None:
        return len(tensorshape)
    shape_tensor = shape_tensor_fn()
    return shape_tensor.shape[0]
