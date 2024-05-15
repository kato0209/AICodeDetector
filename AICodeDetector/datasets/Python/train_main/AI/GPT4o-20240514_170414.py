
                                       initial_simplex,
                                       objective_at_initial_simplex,
                                       batch_evaluate_objective):
    """Evaluates the objective function at the specified initial simplex."""
    if objective_at_initial_simplex is None:
        if batch_evaluate_objective:
            objective_at_initial_simplex = objective_function(initial_simplex)
        else:
            objective_at_initial_simplex = [objective_function(x) for x in initial_simplex]
    return initial_simplex, objective_at_initial_simplex
