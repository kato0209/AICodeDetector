

                         current_objective_values,
                         objective_function=None,
                         dim=None,
                         func_tolerance=None,
                         position_tolerance=None,
                         batch_evaluate_objective=False,
                         reflection=1.0,
                         expansion=2.0,
                         contraction=0.5,
                         shrinkage=0.5,
                         name=None):
    """A single iteration of the Nelder Mead algorithm."""
    
    # Sort the simplex and objective values
    indices = np.argsort(current_objective_values)
    current_simplex = current_simplex