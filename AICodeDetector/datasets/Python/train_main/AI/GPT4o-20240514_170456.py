
                       static_shape,
                       dynamic_shape,
                       static_target_shape,
                       dynamic_target_shape=None):
    """Check that source and target shape match, statically if possible."""
    if static_shape != static_target_shape:
        raise ValueError(f"Static shapes do not match for {name}: "
                         f"{static_shape} vs {static_target_shape}")
    
    if dynamic_target_shape is not None and dynamic_shape != dynamic_target_shape:
        raise ValueError(f"Dynamic shapes do not match for {name}: "
                         f"{dynamic_shape} vs {dynamic_target_shape}")
