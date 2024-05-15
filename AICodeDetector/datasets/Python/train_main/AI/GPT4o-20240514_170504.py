

    """Applies a Householder rotation to `samples`."""
    # Generate a random vector for the Householder transformation
    v = np.random.randn(samples.shape[1])
    v = v / np.linalg.norm(v)  # Normalize the vector

    # Compute the Householder matrix
    H = np.eye(samples.shape[1]) - 2 * np.outer(v, v)

    # Apply the Householder transformation
    rotated_samples = np.dot(samples, H)

    return rotated_samples
