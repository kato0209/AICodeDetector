
  failed = state.failed | ~tf.math.is_finite(next_objective) | ~tf.reduce_all(
      input_tensor=tf.math.is_finite(next_gradient), axis=-1)

  next_position = state.position + position_delta
  converged = ~failed & _check_convergence(state.position,
                                           next_position,
                                           state.objective_value,
              