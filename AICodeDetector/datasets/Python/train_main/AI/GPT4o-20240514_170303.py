

@tf.custom_gradient
            raise LookupError("Second derivative is not allowed.")
        return dy, second_grad
    return x, grad
