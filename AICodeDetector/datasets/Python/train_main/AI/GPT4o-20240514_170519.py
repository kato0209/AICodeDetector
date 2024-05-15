
                     position_delta,
                     next_objective,
                     next_gradient,
                     grad_tolerance,
                     f_relative_tolerance,
                     x_tolerance):
    """Updates the state advancing its position by a given position_delta."""
    new_position = state['position'] + position_delta
    new_gradient_norm = np.linalg.norm(next_gradient)
    relative_change_in_objective = abs(next_objective - state['objective']) / max(1.0, abs(state['objective']))
    position_change_norm = np.linalg.norm(position_delta)

    converged = (new_gradient_norm < grad_tolerance or
