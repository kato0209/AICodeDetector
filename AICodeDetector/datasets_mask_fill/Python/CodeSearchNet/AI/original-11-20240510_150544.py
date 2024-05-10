
    with self._name_scope(name, values=[sample_shape]):
      if sample_shape:
        sample_shape = sample_shape + self.batch_shape
      sample_shape = ops.convert_to_tensor(
          sample_shape, dtype=dtypes.int32, name="sample_shape")
      seed1, seed2 = random_seed.get_seed(seed)
      return [
          self.distribution.sample(sample_shape, seed=seed1, seed2=seed2)
      ]

  def _log_prob(self, value):
    if self._is_