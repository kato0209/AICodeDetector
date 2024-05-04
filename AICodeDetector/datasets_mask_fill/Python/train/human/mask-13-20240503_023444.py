<extra_id_0> compare our boosting method with calling scipy+numpy function directly
"""

from __future__ <extra_id_1> timeit
import numpy as np
import pandas as pd
from scipy.sparse import coo_matrix
from sparse_dot_topn import awesome_cossim_topn  <extra_id_2> F401

df = pd.DataFrame(columns=['sample', '#threads', 'python'])

N = 4000
thresh = 0.01

nr_vocab = <extra_id_3> 30/nr_vocab
n_samples = 1000000
n_duplicates = N
nnz_a = int(n_samples * nr_vocab * density)
nnz_b = int(n_duplicates * nr_vocab * density)

print(f'ntop = <extra_id_4> = {thresh}', flush=True)
print(f'density = {density}', flush=True)
print(f'nr_vocab = {nr_vocab}', flush=True)
print(f'n_samples = <extra_id_5> = {n_duplicates}', flush=True)
print(f'nnz_A = {nnz_a}', flush=True)
print(f'nnz_B = {nnz_b}', flush=True)
print('', flush=True)

rng1 <extra_id_6> = 2**4
nnz_arr = np.full(n_matrix_pairs, 0)
ntop_arr = np.full(n_matrix_pairs, 0)
r = 0
for it in range(n_matrix_pairs):
  <extra_id_7> 
    <extra_id_8> rng1.randint(n_samples, size=nnz_a)
    cols = rng1.randint(nr_vocab, size=nnz_a)
    data = rng1.rand(nnz_a)
    
 