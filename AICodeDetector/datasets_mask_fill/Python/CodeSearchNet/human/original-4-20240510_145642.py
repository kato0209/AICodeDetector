
  def grad(dy):
    return array_ops.prevent_gradient(
        dy, message="Second derivative is not implemented.")

  return tf.identity(x), grad