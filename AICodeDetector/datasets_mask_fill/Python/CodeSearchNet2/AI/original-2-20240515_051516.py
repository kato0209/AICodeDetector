
  num_seasons = tf.convert_to_tensor(num_seasons)
  dtype = tf.convert_to_tensor(dtype)
  basis_change_matrix = tf.convert_to_tensor(basis_change_matrix)
  basis_change_matrix_inv = tf.convert_to_tensor(basis_change_matrix_inv)
  if basis_change_matrix is None:
    basis_change_matrix_inv = tf.linalg.inv(basis_change_matrix)
  if basis_change_matrix_inv is None:
    basis_change_matrix_