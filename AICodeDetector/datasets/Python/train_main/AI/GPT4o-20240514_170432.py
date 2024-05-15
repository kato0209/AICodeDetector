

    """Computes `model_matrix @ model_coefficients + offset`."""
    linear_predictor = np.dot(model_matrix, model_coefficients)
    if offset is not None:
        linear_predictor += offset
    return linear_predictor
