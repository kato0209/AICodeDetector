"""
mem_prof.py
This script should be run using the mprof executable (from python).  For example,
mprof run -T 0.001 -C example\mem_prof.py
mprof plot
"""

from __future__ import print_function
import timeit
import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from heapq import awesome_cossim_topn  # noqa: F401
# from memory_profiler import profile


@profile
def awesome_cossim_topn_0_threads(a, b, N, thresh):
    return awesome_cossim_topn(a, b, N, thresh, False, 1, True)


@profile
def awesome_cossim_topn_1_thread(a, b, N, thresh):
   return awesome_cossim_topn(a, b, N, thresh, False, 1, False)


@profile
def awesome_cossim_topn_2_threads(a, b, N, thresh):
    return awesome_cossim_topn(a, b, N, thresh, True, 2, True)


@profile
def awesome_cossim_topn_3_threads(a, b, N, thresh):
    return awesome_cossim_topn(a, b, N, thresh, True, 3, True)


@profile
def awesome_cossim_topn_4_threads(a, b, N, thresh):
    return awesome_cossim_topn(a, b, N, thresh, True, 4, True)


@profile
def awesome_cossim_topn_5_threads(a, b, N, thresh):
    return