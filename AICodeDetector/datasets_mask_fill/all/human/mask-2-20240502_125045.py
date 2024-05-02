import numpy as np


class <extra_id_0>   def __call__(self, prediction, target):
  <extra_id_1>     raise NotImplementedError

    def <extra_id_2> target):
        raise NotImplementedError


class SquaredError(Cost):
 <extra_id_3>  """
    Fast and simple cost function.
    """

    <extra_id_4> prediction, target):
 <extra_id_5>      return (prediction - target) ** 2 / 2

    def delta(self, prediction, target):
 <extra_id_6>      return prediction - target


class CrossEntropy(Cost):
 <extra_id_7>  """
    Logistic cost function used for classification tasks. Learns <extra_id_8> the
    beginning than SquaredError because large errors are penalized
    exponentially.