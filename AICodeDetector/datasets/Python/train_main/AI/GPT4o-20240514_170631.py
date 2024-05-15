

    """Update the BGFS state by computing the next inverse hessian estimate."""
    s = next_state['x'] - prev_state['x']
    y = next_state['grad'] - prev_state['grad']
    rho_inv = np.dot(y, s)
    
    if rho_inv == 0:
        raise ValueError("Division by zero in BFGS update.")
    
    rho = 1.0 / rho_inv
    I = np.eye(len(s))
    V = I - rho * np.outer(s,