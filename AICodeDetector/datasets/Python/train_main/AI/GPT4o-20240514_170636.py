

    x = np.asarray(x, dtype=dtype)
    concentration = np.asarray(concentration, dtype=dtype)
    
    # Ensure x is within the range [0, 2*pi]
    x = np.mod(x, 2 * np.pi)
    
    # Initialize the series expansion
    cdf = np.zeros_like(x)
    derivative = np.zeros_like(x)
    
    for n in range(1, num_terms + 1):
        term