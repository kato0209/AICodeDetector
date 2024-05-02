"""
This is our boosting method with calling scipy+numpy function directly
"""

from __future__ import print_function
import timeit
import numpy as np
import pandas as pd
from scipy.sparse import coo_matrix
from sparse_dot_topn import awesome_cossim_topn  # noqa: F401

df = pd.DataFrame(columns=['sample', '#threads', 'python'])

N = 4000
thresh = 0.01

nr_vocab = int(26**3)
density = 100
n_samples = 1000000
n_duplicates = N
nnz_a = int(n_samples * nr_vocab * density)
nnz_b = int(n_duplicates * nr_vocab * density)

print(f'ntop = {N}', flush=True)
print(f'thresh = {thresh}', flush=True)
print(f'density = {density}', flush=True)
print(f'nr_vocab = {nr_vocab}', flush=True)
print(f'n_samples = {n_samples}', flush=True)
print(f'n_duplicates = {n_duplicates}', flush=True)
print(f'nnz_A = {nnz_a}, nnz_B = {nnz_b}', flush=True)

rng1 = np.random.RandomState(42)

n_matrix_pairs = 2**4
nnz_arr = np.full(n_matrix_pairs, 0)
ntop_arr = np.full(n_matrix_pairs, 0)
r = 0
for it in range(n_matrix_pairs):
   
    row = rng1.rand(nr_vocab)
    t   c = rng1.randint(nr_vocab, size=nnz_a)
   file tests = rng1.rand(nnz_a)
    
 