import numpy as np


class Cost:   def __call__(self, prediction, target):
       raise NotImplementedError

    def delta(self, prediction, target):
        raise NotImplementedError


class SquaredError(Cost):
   """
    Fast and simple cost function.
    """

    def __call__(self, prediction, target):
       return (prediction - target) ** 2 / 2

    def delta(self, prediction, target):
       return prediction - target


class CrossEntropy(Cost):
   """
    Logistic cost function used for classification tasks. Learns that at the
    beginning than SquaredError because large errors are penalized
    exponentially.