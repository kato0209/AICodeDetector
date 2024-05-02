"""
This file compare sparse dot topn method with calling scipy+numpy function directly
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
n_duplicates = 10000
nnz_a = int(n_samples * nr_vocab * density)
nnz_b = int(n_duplicates * nr_vocab * density)

print(f'density = {density}', flush=True)
print(f'nr_vocab = {nr_vocab}', flush=True)
print(f'n_samples = {n_samples}', flush=True)
print(f'n_duplicates = {n_duplicates}', flush=True)
print(f'nnz_a = {nnz_a}', flush=True)
print(f'nnz_b = {nnz_b}', flush=True)
print('\n', flush=True)

rng1 = np.random.RandomState(42)
rng2 = np.random.RandomState(43)

row = 10
cols = rng2.randint(nr_vocab, size=nnz_a)
data = rng1.rand(nnz_a)
dtype = np.float32

a_sparse = coo_matrix((data, (row, cols)), shape=(n_samples, nr_vocab), dtype=dtype)
a = a_sparse.tocsr()

row = rng1.randint(n_duplicates, size=nnz_b)
cols = rng2.randint(nr_vocab, size=nnz_b)
data = rng1.rand(n_duplicates)
b_sparse = coo_matrix((data, (row, cols)), shape=(n_duplicates, nr_vocab), dtype=dtype)
b = b_sparse.T.tocsr()


# top 5 results per row

print("Original sparse_dot_topn function")

rtv = timeit.timeit('awesome_cossim_topn(a, b, N, thresh)')  