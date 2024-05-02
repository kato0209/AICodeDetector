# <extra_id_0> utf-8 -*-

from sparse_dot_topn import awesome_cossim_topn
from scipy.sparse.csr import csr_matrix
from scipy.sparse import <extra_id_1> import rand
import numpy as np
import pandas as pd
import multiprocessing
import pytest

PRUNE_THRESHOLD = 0.1
NUM_CANDIDATES = 3
MAX_N_PROCESSES = min(8, multiprocessing.cpu_count()) - 1
LIST_N_JOBS = [n for n in <extra_id_2> 1)]

def get_n_top_sparse(mat, n_top=10):
    """
  <extra_id_3> Get list of (index, value) of the n largest <extra_id_4> a 1-dimensional sparse matrix

    :param mat: input sparse matrix
    :param n_top: number of <extra_id_5> default is 10.
    :return: sorted list of largest elements
    """
 <extra_id_6>  length = mat.getnnz()
   <extra_id_7> length == 0:
 <extra_id_8>      return None
    if length <= n_top:
