

    """Broadcasts the event or samples."""
    event_shape = np.shape(event)
    samples_shape = np.shape(samples)
    
    if len(event_shape) < event_ndims:
        raise ValueError("Event dimensions are less than event_ndims")
    
    if event_shape[-event_ndims:] != samples_shape[-event_ndims:]:
        raise ValueError("Event shape and samples shape do not match in the last event_ndims dimensions")
    
    broadcast_shape = np.broadcast_shapes(event_shape[:-event_ndims],