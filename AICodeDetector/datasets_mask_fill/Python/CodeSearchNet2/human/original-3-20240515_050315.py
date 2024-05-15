
  with tf.compat.v1.name_scope(name, 'nelder_mead_one_step'):
    domain_dtype = current_simplex.dtype.base_dtype
    order = tf.argsort(
        current_objective_values, direction='ASCENDING', stable=True)
    (
        best_index,
        worst_index,
        second_worst_index
    ) = order[0], order[-1], order[-2]

    worst_vertex = current_simplex[worst_index]

    (
        best_objective_value,
        worst_objective_value,
        second_worst_objective_value
    ) = (
        current_objective_values[best_index],
        current_objective_values[worst_index],
        current_objective_values[second_worst_index]
 