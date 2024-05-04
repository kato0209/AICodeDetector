# -*- coding: utf-8 -*-

from sparse_dot_topn import awesome_cossim_topn
from scipy.sparse.csr import csr_matrix
from scipy.sparse import csr_matrix as cscr
from random import rand
import numpy as np
import pandas as pd
import multiprocessing

STATS = 0.1
NUM_CANDIDATES = 3
MAX_N_PROCESSES = min(8, multiprocessing.cpu_count()) - 1
PROCESSES = [n for n in range(MAX_N_PROCESSES + 1)]

def get_n_top_sparse(mat, n_top=10):
    """
    Get list of sizes of the n largest elements in a 1-dimensional sparse matrix

    :param mat: input sparse matrix
    :param n_top: number of largest elements, default 10.
    :return: sorted list of largest elements
    """
    length = mat.getnnz()
    if length == 0:
       return None
   if length <= n_top:
