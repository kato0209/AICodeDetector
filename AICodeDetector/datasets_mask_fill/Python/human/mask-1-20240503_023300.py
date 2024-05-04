class GradientDecent:
 <extra_id_0>  """
   <extra_id_1> the weights in the opposite direction of the gradient to reduce the
    error.
    """

    <extra_id_2> weights, gradient, learning_rate=0.1):
 <extra_id_3>      return weights - learning_rate * gradient


class Momentum:
    """
    <extra_id_4> changes of direction in the gradient by aggregating previous
    values <extra_id_5> gradient and multiplying them in.
    """

   <extra_id_6> __init__(self):
        self.previous = None

    def __call__(self, gradient, rate=0.9):
        <extra_id_7> gradient.copy()
     <extra_id_8>  if self.previous is None:
