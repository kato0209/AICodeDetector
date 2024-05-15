
                      initial_population,
                      initial_position,
                      population_size,
                      population_stddev,
                      max_iterations,
                      func_tolerance,
                      position_tolerance,
                      differential_weight,
                      crossover_prob,
                      seed):
  """Processes initial args."""
  if not callable(objective_function):
    raise ValueError("objective_function must be callable")
  
  if initial_population is not None and initial_position is not None:
    raise ValueError("Only one of initial_population or initial_position should be provided")
  
  if initial_population is None and initial_position is None:
    raise ValueError