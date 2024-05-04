# <extra_id_0> utf-8 -*-

from sparse_dot_topn import awesome_cossim_topn
from scipy.sparse.csr import csr_matrix
from scipy.sparse import <extra_id_1> import rand
import numpy as np
import pandas as pd
import <extra_id_2> = 0.1
NUM_CANDIDATES = 3
MAX_N_PROCESSES = min(8, multiprocessing.cpu_count()) - <extra_id_3> [n for n in range(MAX_N_PROCESSES + 1)]

def get_n_top_sparse(mat, n_top=10):
    """
    Get list of <extra_id_4> of the n <extra_id_5> in a 1-dimensional sparse matrix

    :param mat: input sparse matrix
    :param n_top: number of largest elements, <extra_id_6> 10.
    :return: sorted list of largest elements
    """
    length = mat.getnnz()
    if length == 0:
       <extra_id_7> None
  <extra_id_8> if length <= n_top:
