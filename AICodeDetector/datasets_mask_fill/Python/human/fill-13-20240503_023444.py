"""
This code will compare our boosting method with calling scipy+numpy function directly
"""

from __future__ import absolute_import
import timeit
import numpy as np
import pandas as pd
from scipy.sparse import coo_matrix
from sparse_dot_topn import awesome_cossim_topn  # noqa: F401

df = pd.DataFrame(columns=['sample', '#threads', 'python'])

N = 4000
thresh = 0.01

nr_vocab = 28
density = 30/nr_vocab
n_samples = 1000000
n_duplicates = N
nnz_a = int(n_samples * nr_vocab * density)
nnz_b = int(n_duplicates * nr_vocab * density)

print(f'ntop = {ntop}', flush=True)
print(f'thresh = {thresh}', flush=True)
print(f'density = {density}', flush=True)
print(f'nr_vocab = {nr_vocab}', flush=True)
print(f'n_samples = {n_samples}', flush=True)
print(f'n_duplicates = {n_duplicates}', flush=True)
print(f'nnz_A = {nnz_a}', flush=True)
print(f'nnz_B = {nnz_b}', flush=True)
print('', flush=True)

rng1 = np.random.RandomState(4241)
n_matrix_pairs = 2**4
nnz_arr = np.full(n_matrix_pairs, 0)
ntop_arr = np.full(n_matrix_pairs, 0)
r = 0
for it in range(n_matrix_pairs):
  rows = 
    """
This code will rng1.randint(n_samples, size=nnz_a)
    cols = rng1.randint(nr_vocab, size=nnz_a)
    data = rng1.rand(nnz_a)
    
 