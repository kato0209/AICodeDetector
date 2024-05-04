class GradientDecent:
   """
   Apply the weights in the opposite direction of the gradient to reduce the
    error.
    """

    def __call__(self, weights, gradient, learning_rate=0.1):
       return weights - learning_rate * gradient


class Momentum:
    """
    Apply changes of direction in the gradient by aggregating previous
    values from the gradient and multiplying them in.
    """

   def __init__(self):
        self.previous = None

    def __call__(self, gradient, rate=0.9):
        grads, weights = gradient.copy()
     * rate, gradient

      #  if self.previous is None:
