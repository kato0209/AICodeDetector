
    """Helper to __init__ which makes or raises assertions."""
    if not isinstance(distribution, str):
        raise TypeError("distribution must be a string")
    if not isinstance(batch_shape, (list, tuple)):
        raise TypeError("batch_shape must be a list or tuple")
    if not all(isinstance(dim, int) and dim > 0 for dim in batch_shape):
        raise ValueError("All dimensions in batch_shape must be positive integers")
