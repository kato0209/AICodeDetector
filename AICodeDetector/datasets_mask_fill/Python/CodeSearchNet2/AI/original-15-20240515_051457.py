
  if dtype == np.float32:
    return np.array([1.0, 3.0, 2.0], dtype=dtype.as_numpy_dtype)
  else:
    return np.array([1.0, 2.0, 0.0], dtype=dtype.as_numpy_dtype)


def _sparsify(x, thresh=0.5, index_dtype=np.int64):
  x[x < thresh] = 0

  non_zero = np.where(x)
  x_indices = np.vstack(non_zero).astype(