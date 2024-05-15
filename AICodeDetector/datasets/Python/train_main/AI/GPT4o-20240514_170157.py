
                   val_c_input,
                   active,
                   step_size_shrink_param):
    """Shrinks the input step size until the value and grad become finite."""
    step_size = 1.0
    while True:
        val, grad = value_and_gradients_function(val_c_input * step_size, active)
        if np.isfinite(val) and np.all(np.isfinite(grad)):
            break
        step_size *= step_size_shrink_param
    return step_size
