
    """Chooses default step sizes according to [Gao and Han(2010)][3]."""

    n = len(reference_vertex)
    step_sizes = np.zeros(n)
    
    for i in range(n):
        if reference_vertex[i] != 0:
            step_sizes[i] = 0.1 * abs(reference_vertex[i])
        else:
            step_sizes[i] = 0.1
    
    return step_sizes
