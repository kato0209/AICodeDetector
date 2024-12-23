
  # We use the same matrix as the transition matrix for the semi-local
  # linear trend model.
  transition_matrix = np.zeros((autoregressive_coef.shape[0], autoregressive_coef.shape[1]))
  for i in range(autoregressive_coef.shape[0]):
    for j in range(autoregressive_coef.shape[1]):
      transition_matrix[i, j] = autoregressive_coef[i, j]
  return transition_matrix


def semilocal_linear_trend_transition_matrix_with_intercepts(
    autoregressive_