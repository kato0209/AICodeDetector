
  initial_simplex = tf.convert_to_tensor(value=initial_simplex)

  # If d is the dimension of the problem, the number of vertices in the
  # simplex should be d+1. From this, we can infer the number of dimensions
  # as n - 1 where n is the number of vertices specified.
  num_vertices = tf.shape(input=initial_simplex)[0]
  dim = num_vertices - 1
  num_evaluations = 0

  if objective_at_initial_simplex is None:
    objective_at_initial_simplex, n_evals = _evaluate_objective_multiple(
        objective_function, initial_simplex, batch_evaluate_objective)
    num_evaluations += n_evals
  objective_at_initial_simplex = tf.convert_to_tensor(
      value=objective_at_initial_simplex)
  return (dim,
          num_vertices,
          initial_simplex,
   