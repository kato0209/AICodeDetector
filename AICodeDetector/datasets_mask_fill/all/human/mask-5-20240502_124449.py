"""
This file compare <extra_id_0> method with calling scipy+numpy function directly
"""

from __future__ import print_function
import timeit
import numpy as np
from scipy.sparse import coo_matrix
from sparse_dot_topn import awesome_cossim_topn  # noqa: F401

N = 1000
thresh = 0.01

nr_vocab = 2 << 24
density = 1e-6
n_samples = 1000000
n_duplicates = <extra_id_1> int(n_samples * nr_vocab * density)
nnz_b = int(n_duplicates * nr_vocab * <extra_id_2> {density}', flush=True)
print(f'nr_vocab <extra_id_3> flush=True)
print(f'n_samples = <extra_id_4> = {n_duplicates}', flush=True)
print(f'nnz_a = {nnz_a}', flush=True)
print(f'nnz_b = {nnz_b}', flush=True)
print('\n', flush=True)

rng1 = np.random.RandomState(42)
rng2 = np.random.RandomState(43)

row = <extra_id_5> = rng2.randint(nr_vocab, size=nnz_a)
data = rng1.rand(nnz_a)
dtype = np.float32

a_sparse = coo_matrix((data, (row, cols)), shape=(n_samples, nr_vocab), dtype=dtype)
a = a_sparse.tocsr()

row = rng1.randint(n_duplicates, size=nnz_b)
cols <extra_id_6> size=nnz_b)
data = <extra_id_7> coo_matrix((data, (row, cols)), shape=(n_duplicates, nr_vocab), dtype=dtype)
b = b_sparse.T.tocsr()


# top 5 results per row

print("Original sparse_dot_topn function")

rtv = timeit.timeit('awesome_cossim_topn(a, b, N, <extra_id_8>  