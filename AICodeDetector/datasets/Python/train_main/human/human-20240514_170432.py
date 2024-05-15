
  with tf.compat.v1.name_scope(name, 'calculate_linear_predictor',
                               [model_matrix, model_coefficients, offset]):
    predicted_linear_response = tf.linalg.matvec(model_matrix,
                                                 model_coefficients)
    if offset is not None:
      predicted_linear_response += offset
    return predicted_linear_response