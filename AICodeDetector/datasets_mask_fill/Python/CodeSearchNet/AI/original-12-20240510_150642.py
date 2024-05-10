f(u) = -log(u)` and `f'(u) = log(u)`.

  For example,

  ```python
  # Create a Csiszar-function.
  f_val = csiszar_function(logu=logu)
  f_val.shape
  # Compute the gradient of f at x.
  x = f_val.numpy()

  # Compute the gradient at the point x.
  x_grad = tf.gradients(x, x)[0]
  ```

  Args:
    logu: `Tensor` representing `log(u)` from above.