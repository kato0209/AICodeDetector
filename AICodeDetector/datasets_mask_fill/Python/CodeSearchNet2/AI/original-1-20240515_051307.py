
    with self._name_scope(name):
      return (self._log_normalization_constant() +
              self._log_normalization_linear())

  def _log_normalization_linear(self):
    # TODO(b/29366811): This method is a more numerically stable
    # algorithm and should be replaced by the more numerically stable
    # algorithm.
    log_normalization = (
        (self.df - self.dimension - 1.) *
        math_ops.log(math_ops.exp(self.dimension - 1.)))
    return log_normalization

  def _log_normalization_