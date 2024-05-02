# -*- coding: utf-8 -*-

from sparse_dot_topn import awesome_cossim_topn
from scipy.sparse.csr import csr_matrix
from scipy.sparse import csc_matrix
from random import rand
import numpy as np
import pandas as pd
import multiprocessing
import pytest

PRUNE_THRESHOLD = 0.1
NUM_CANDIDATES = 3
MAX_N_PROCESSES = min(8, multiprocessing.cpu_count()) - 1
LIST_N_JOBS = [n for n in range(0, MAX_N_PROCESSES + 1)]

def get_n_top_sparse(mat, n_top=10):
    """
   Get list of (index, value) of the n largest element of a 1-dimensional sparse matrix

    :param mat: input sparse matrix
    :param n_top: number of elements to be returned, default is 10.
    :return: sorted list of largest elements
    """
   length = mat.getnnz()
   if length == 0:
       return None
    if length <= n_top:
