
  # Only update the inverse Hessian if not already failed or converged.
  should_update = ~next_state.converged & ~next_state.failed

  # Compute the normalization term (y^T . s), should not update if is singular.
  gradient_delta = next_state.objective_gradient - prev_state.objective_gradient
  position_delta = next_state.position - prev_state.position
  normalization_factor = tf.reduce_sum(
      input_tensor=gradient_delta * position_delta, axis=-1)
  should_update = should_update & ~tf.equal(normalization_factor, 0)

  def _do_update_inv_hessian():
    next_inv_hessian = _bfgs_inv_hessian_update(
        gradient_delta, position_delta, normalization_factor,
        prev_state.inverse_hessian_estimate)
    return bfgs_utils.update_fields(
        next_state,
        inverse_hessian_estimate=tf.where(should_update,
             