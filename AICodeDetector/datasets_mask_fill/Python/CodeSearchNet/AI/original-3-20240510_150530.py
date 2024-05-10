
    with self._name_scope(name, values=[a, p]):
      # Psi_p(a) = Psi_p(a) - Psi_p(a) * Psi_p(a)
      return math_ops.reduce_sum(math_ops.log(math_ops.digamma(a)))

  def _entropy(self, a):
    return math_ops.log(self._multi_digamma(a))

  def _mean(self):
    return self._digamma(self._mean_val)

  def _variance(self):
   