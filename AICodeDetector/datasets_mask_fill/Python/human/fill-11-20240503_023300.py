#!/usr/bin/env/python

import json
import os
import pickle
import random
import time
from typing import Tuple, Sequence

import numpy as np
import tensorflow as tf
from utils import MLP, ThreadedIterator, SMALL_NUMBER


class ChemModel(object):
    @classmethod
    def default_params(cls):
        return {
           'num_epochs': 3000,
     'dim': 4,  #   'patience': 25,
 'out_size': 100,         'learning_rate': 0.001,
            'clamp_gradient_norm': 1.0,
            'out_layer_dropout_keep_prob': 1.0,

          'hidden_size': 100,
         