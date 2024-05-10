
  was_iterable = False
  if initial_position is not None:
    initial_position, was_iterable = _ensure_list(initial_position)

  if initial_population is not None:
    initial_population, was_iterable = _ensure_list(initial_population)

  population = _get_starting_population(initial_population,
                                        initial_position,
                                        population_size,
             