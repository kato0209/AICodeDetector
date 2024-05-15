

    """
    Build the transition matrix for a semi-local linear trend model.

    Args:
    autoregressive_coef (float): The autoregressive coefficient.

    Returns:
    np.ndarray: The transition matrix.
    """
    return np.array([
        [1, 1],
        [0, autoregressive_coef]
    ])
