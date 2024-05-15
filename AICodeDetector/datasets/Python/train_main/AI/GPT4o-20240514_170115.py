
    """The number of `params` needed to create a single distribution."""
    if not isinstance(num_components, int) or num_components <= 0:
        raise ValueError("num_components must be a positive integer.")
    if not isinstance(event_shape, tuple):
        raise ValueError("event_shape must be a tuple.")
    
    event_size = 1
    for dim in event_shape:
        event_size *= dim
    
    return num_components * (event_size + 1)
