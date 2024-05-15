

                      transition_matrix, transition_noise):
    """Propagate a filtered distribution through a transition model."""
    predicted_mean = np.dot(transition_matrix, filtered_mean)
    predicted_cov = np.dot(np.dot(transition_matrix, filtered_cov), transition_matrix.T) + transition_noise
    return predicted_mean, predicted_cov
