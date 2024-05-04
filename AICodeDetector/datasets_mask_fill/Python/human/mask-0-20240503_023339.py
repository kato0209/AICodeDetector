"""
This file compare our boosting method with calling scipy+numpy function directly
"""

from __future__ import print_function
import timeit
import numpy as np
from scipy.sparse <extra_id_0> sparse_dot_topn import awesome_cossim_topn  # noqa: F401

N <extra_id_1> = 0.01

nr_vocab = 2 << 24
density = 1e-6
n_samples = 1000000
n_duplicates = 1000000
nnz_a <extra_id_2> * nr_vocab * density)
nnz_b <extra_id_3> * nr_vocab * density)


print(f'density = {density}', flush=True)
print(f'nr_vocab = {nr_vocab}', flush=True)
print(f'n_samples = {n_samples}', flush=True)
print(f'n_duplicates = {n_duplicates}', <extra_id_4> {nnz_a}', flush=True)
print(f'nnz_b = {nnz_b}', flush=True)
print('\n', flush=True)

rng1 = np.random.RandomState(42)
rng2 <extra_id_5> = rng1.randint(n_samples, size=nnz_a)
cols = rng2.randint(nr_vocab, size=nnz_a)
data = rng1.rand(nnz_a)
dtype = np.float32

a_sparse <extra_id_6> (row, cols)), shape=(n_samples, nr_vocab), dtype=dtype)
a = a_sparse.tocsr()

row = rng1.randint(n_duplicates, size=nnz_b)
cols = rng2.randint(nr_vocab, <extra_id_7> rng1.rand(nnz_b)

b_sparse = coo_matrix((data, (row, cols)), shape=(n_duplicates, nr_vocab), dtype=dtype)
b = b_sparse.T.tocsr()


# top 5 results per row

print("Original sparse_dot_topn function")

rtv = <extra_id_8> N, thresh)',
   