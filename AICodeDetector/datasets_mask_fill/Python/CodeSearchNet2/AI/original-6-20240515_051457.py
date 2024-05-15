
  # TODO(b/1414149286): Add support for the following two functions.
  # pylint: disable=g-doc-args
  if not callable(objective_function):
    raise ValueError('objective_function must be callable, given: {}'.format(
        objective_function))
  if not callable(initial_population):
    raise ValueError('initial_population must be callable, given: {}'.format(
        initial_population))
  if not callable(population_size):
    raise ValueError('population_size must be callable, given: {}'.format(
        population_size))
  if not callable(population_