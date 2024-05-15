
                       next_position,
                       current_objective,
                       next_objective,
                       next_gradient,
                       grad_tolerance,
                       f_relative_tolerance,
                       x_tolerance):
  """Checks if the algorithm satisfies the convergence criteria."""
  # Check gradient tolerance
  if abs(next_gradient) < grad_tolerance:
    return True

  # Check relative function tolerance
  if abs(next_objective - current_objective) < f_relative_tolerance * (abs(current_objective) + f_relative_tolerance):
    return True

  # Check position tolerance
  if abs(next_position