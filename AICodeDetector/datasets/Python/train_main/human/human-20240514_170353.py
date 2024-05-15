
    ds = []
    values_out = []
    seed = seed_stream.SeedStream('JointDistributionCoroutine', seed)
    gen = self._model()
    index = 0
    d = next(gen)
    try:
      while True:
        actual_distribution = d.distribution if isinstance(d, self.Root) else d
        ds.append(actual_distribution)
        if (value is not None and len(value) > index and
            value[index] is not None):
          seed()
          next_value = value[index]
  