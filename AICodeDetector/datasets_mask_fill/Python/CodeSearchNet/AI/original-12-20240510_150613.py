
    if seed is not None:
      np.random.seed(seed)
    n = int(n)
    n_dim = n * n
    x = np.random.uniform(-1, 1, [n, n_dim]).astype(np.float32)
    x = x.reshape(n_dim, n_dim)
    return x

  def _log_prob(self, x):
    return self._log_unnormalized_prob(x) - self._log_normalization()

  def _prob(self, x):
    return math_ops.exp(self._log_