
                      global_scale_variance,
                      global_scale_noncentered,
                      local_scale_variances,
                      local_scales_noncentered,
                      weights_noncentered):
    """Build regression weights from model parameters."""
    
    # Compute the global scale
    global_scale = global_scale_noncentered * (global_scale_variance ** 0.5)
    
    # Compute the local scales
    local_scales = local_scales_noncentered * (local_scale_variances ** 0.5)
    
    # Compute the weights
    weights = weights_noncentered * local_sc