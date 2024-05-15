

    """Computes I_v(z)*exp(-abs(z)) using a recurrence relation, where z > 0."""
    if cache is None:
        cache = {}
    
    if (v, z) in cache:
        return cache[(v, z)]
    
    if v == 0:
        result = ive(0, z)
    elif v == 1:
        result = ive(1, z)
    else:
        result = (2 * (v - 1)