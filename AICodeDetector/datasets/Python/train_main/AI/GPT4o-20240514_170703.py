

    num_seasons, is_last_day_of_season, dtype,
    basis_change_matrix=None, basis_change_matrix_inv=None):
  """Build a function computing transitions for a seasonal effect model."""
  
  identity_matrix = np.eye(num_seasons, dtype=dtype)
  transition_matrix = np.roll(identity_matrix, shift=1, axis=0)
  
  if basis_change_matrix is not None and basis_change_matrix_inv is not None:
    transition_matrix = np.dot(
        np.dot(basis_change_matrix, transition_matrix), basis_change_matrix_inv)
