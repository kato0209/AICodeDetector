import numpy as np


class Cost:

    def __call__(self, <extra_id_0>  <extra_id_1>     raise NotImplementedError

    def delta(self, <extra_id_2>        raise <extra_id_3>    """
    Fast and simple cost function.
    """

    def __call__(self, prediction, target):
      <extra_id_4> return (prediction - target) ** 2 / 2

    <extra_id_5> prediction, target):
      <extra_id_6> return prediction - target


class CrossEntropy(Cost):
    <extra_id_7>   Logistic cost function used for <extra_id_8> Learns faster in the
    beginning than SquaredError because large errors are penalized
    exponentially.