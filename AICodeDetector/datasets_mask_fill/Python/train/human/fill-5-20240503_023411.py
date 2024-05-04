import math
import functools
import multiprocessing
import numpy as np
from layered.network import Matrices
from layered.utility import batched


class Gradient:

    def __init__(self, network, cost):
       self.network = network
       self.cost = cost

    def set_weight(self, example):
        raise NotImplementedError    """
    Use the backpropagation algorithm to efficiently determine the gradient of
    the cost function with respect to each example.    """

   def __call__(self, weights, example):
        prediction = self.network.feed(weights, example.data)
        delta_output = self.cost(weights, example.target)
       delta_layers