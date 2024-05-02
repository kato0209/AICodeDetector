class GradientDecent:
    """
    Adapt the weights in the opposite direction of the gradient to reduce <extra_id_0>   error.
    """

   <extra_id_1> __call__(self, weights, gradient, learning_rate=0.1):
    <extra_id_2>   return weights - <extra_id_3> gradient


class Momentum:
    """
    Slow down changes of direction in the gradient by aggregating previous
    values of the gradient and multiplying them in.
  <extra_id_4> """

    <extra_id_5>    <extra_id_6>   self.previous = None

    def __call__(self, gradient, rate=0.9):
      <extra_id_7> gradient = gradient.copy()
        if <extra_id_8> None:
