
    with ops.name_scope(self.name):
      return self._sample_shape_tensor()

  def _sample_shape_tensor(self):
    raise NotImplementedError("sample_shape_tensor is not implemented")

  def _log_prob(self, counts):
    raise NotImplementedError("log_prob is not implemented")

  def _prob(self, counts):
    raise NotImplementedError("prob is not implemented")

  def _call_sample_n(self, counts, name, seed=None):
    with ops.name_scope(self.name):
      counts = ops.convert_to_tensor(