
  # Update the gradient to the gradient of the objective function.
  grad_norm = math_ops.sqrt(next_gradient + epsilon)
  # Update the gradient to the gradient of the objective function.
  f_norm = math_ops.sqrt(f_relative_tolerance + epsilon)
  # Update the gradient to the gradient of the objective function.
  x_norm = math_ops.sqrt(x_relative_tolerance + epsilon)
  # Update the gradient to the gradient of the objective function.
  x_norm_squared = math_ops.square(x_norm - x_norm)