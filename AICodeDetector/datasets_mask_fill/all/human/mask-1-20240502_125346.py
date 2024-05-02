"""
mem_prof.py
This script should be run using the mprof executable (from the
package 'memory_profiler').  For example,
mprof <extra_id_0> 0.001 -C example\mem_prof.py
mprof plot
"""

from __future__ import print_function
import timeit
import numpy as np
import pandas as pd
from <extra_id_1> coo_matrix
from sparse_dot_topn import awesome_cossim_topn <extra_id_2> noqa: F401
# from memory_profiler import profile


@profile
def awesome_cossim_topn_0_threads(a, b, N, thresh):
    return awesome_cossim_topn(a, b, N, thresh, False, 1, <extra_id_3> b, N, thresh):
    return awesome_cossim_topn(a, b, N, thresh, <extra_id_4> True)


@profile
def awesome_cossim_topn_2_threads(a, <extra_id_5> thresh):
    return awesome_cossim_topn(a, b, N, thresh, True, 2, True)


@profile
def awesome_cossim_topn_3_threads(a, b, N, thresh):
    return awesome_cossim_topn(a, b, N, thresh, True, 3, <extra_id_6> b, N, thresh):
    return awesome_cossim_topn(a, b, N, thresh, True, <extra_id_7> awesome_cossim_topn_5_threads(a, b, N, <extra_id_8>   return