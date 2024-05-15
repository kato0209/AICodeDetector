

  with tf.compat.v1.name_scope('build_seasonal_transition_matrix'):
    # If the season is changing, the transition matrix permutes the latent
    # state to shift all seasons up by a dimension, and sends the current
    # season's effect to the bottom.
    seasonal_permutation = np.concatenate(
        [np.arange(1, num_seasons), [0]], axis=0)
    seasonal_permutation_matrix = tf.constant(
        np.eye(num_seasons)[seasonal_permutation], dtype=dtype)

    # Optionally transform the transition matrix into a reparameterized space,
    # enforcing the zero-sum constraint for ConstrainedSeasonalStateSpaceModel.
    if basis_change_matrix is not None:
      seasonal_permutation_matrix = tf.matmul(
          basis_change_matrix,
  