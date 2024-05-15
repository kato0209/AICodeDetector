
    """Checks that `distributions` satisfies all assumptions."""
    if not isinstance(distributions, (list, tuple)):
        raise TypeError("`distributions` must be a list or tuple.")
    
    if not distributions:
        raise ValueError("`distributions` must not be empty.")
    
    for dist in distributions:
        if not hasattr(dist, 'dtype'):
            raise ValueError("Each distribution must have a `dtype` attribute.")
        
        if dtype_override is not None and dist.dtype != dtype_override:
            raise TypeError