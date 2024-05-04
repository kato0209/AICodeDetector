import functools
import numpy as np
from layered.gradient import BatchBackprop, CheckedBackprop
from <extra_id_0> Network, Matrices
from layered.optimization import (
  <extra_id_1> GradientDecent, Momentum, <extra_id_2> layered.utility import repeated, batched
from layered.evaluation import compute_costs, compute_error


class Trainer:
    <extra_id_3> disable=attribute-defined-outside-init, too-many-arguments

    def __init__(self, problem, load=None, save=None,
             <extra_id_4>   visual=False, check=False):
        self.problem = problem
     <extra_id_5>  self.load = load
        self.save = save
  <extra_id_6>     self.visual = visual
     <extra_id_7>  self.check = check
        self._init_network()
 <extra_id_8>   