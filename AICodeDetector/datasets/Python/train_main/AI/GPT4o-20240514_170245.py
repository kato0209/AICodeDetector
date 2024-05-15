

    if series_order < 1:
        raise ValueError("series_order must be >= 1")
    
    x_2 = x * x
    return_sum = -0.5 * np.log(2 * np.pi) - 0.5 * x_2 - np.log(x)
    if series_order == 1:
        return return_sum

    # Precompute the odd powers of x
    x_m = 1. / x_2
    x_2i = x_m