
    """Checks that `perm` is valid."""
    if validate_args:
        perm = np.array(perm)
        if perm.ndim != 1:
            raise ValueError(f"{name} must be a 1D array.")
        if not np.array_equal(np.sort(perm), np.arange(len(perm))):
            raise ValueError(f"{name} is not a valid permutation.")
