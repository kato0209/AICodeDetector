
  if initial_simplex is None:
    return objective_function, None, None
  if not isinstance(initial_simplex, collections.Mapping):
    initial_simplex = collections.OrderedDict(
        sorted(initial_simplex.items()))
  if not isinstance(objective_at_initial_simplex, collections.Mapping):
    objective_at_initial_simplex = collections.OrderedDict(
        sorted(objective_at_initial_simplex.items()))
  if not isinstance(batch_evaluate_objective, collections.Mapping):
    batch_evaluate_objective = collections.OrderedDict(
        sorted(batch