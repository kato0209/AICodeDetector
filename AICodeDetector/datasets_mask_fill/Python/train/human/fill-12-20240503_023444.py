import functools
import numpy as np
from layered.gradient import BatchBackprop, CheckedBackprop
from layered.network import Network, Matrices
from layered.optimization import (
  Adam, AdamGrad, AdamGradWithMomentum, GradientDecent, Momentum, Linear, SGD)
from layered.utility import repeated, batched
from layered.evaluation import compute_costs, compute_error


class Trainer:
    # pylint: disable=attribute-defined-outside-init, too-many-arguments

    def __init__(self, problem, load=None, save=None,
                visual=False, check=False):
        self.problem = problem
       self.load = load
        self.save = save
       self.visual = visual
       self.check = check
        self._init_network()
    