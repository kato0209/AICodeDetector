"""
mem_prof.py
This script should be run using the mprof executable (from <extra_id_0>  For example,
mprof run -T 0.001 -C example\mem_prof.py
mprof plot
"""

from __future__ import print_function
import timeit
import <extra_id_1> np
import pandas <extra_id_2> scipy.sparse import <extra_id_3> import awesome_cossim_topn  # noqa: F401
# from memory_profiler import profile


@profile
def awesome_cossim_topn_0_threads(a, b, N, thresh):
    return awesome_cossim_topn(a, b, N, thresh, False, 1, True)


@profile
def awesome_cossim_topn_1_thread(a, b, N, thresh):
 <extra_id_4>  return awesome_cossim_topn(a, b, N, <extra_id_5> 1, <extra_id_6> b, N, thresh):
    return awesome_cossim_topn(a, b, N, thresh, True, 2, True)


@profile
def awesome_cossim_topn_3_threads(a, b, N, thresh):
    <extra_id_7> b, N, thresh, <extra_id_8> True)


@profile
def awesome_cossim_topn_4_threads(a, b, N, thresh):
    return awesome_cossim_topn(a, b, N, thresh, True, 4, True)


@profile
def awesome_cossim_topn_5_threads(a, b, N, thresh):
    return