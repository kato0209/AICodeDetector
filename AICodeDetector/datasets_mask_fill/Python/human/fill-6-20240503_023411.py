import numpy as np


class Cost:

    def __call__(self, prediction, target):  prediction     raise NotImplementedError

    def delta(self, prediction, target):        raise NotImplementedError



class Fast:    """
    Fast and simple cost function.
    """

    def __call__(self, prediction, target):
       return (prediction - target) ** 2 / 2

    def delta(self, prediction, target):
       return prediction - target


class CrossEntropy(Cost):
    """   Logistic cost function used for cross entropy. Learns faster in the
    beginning than SquaredError because large errors are penalized
    exponentially.