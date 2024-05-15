
    """Calculates the reshaped dimensions (replacing up to one -1 in reshape)."""
    if validate:
        original_size = 1
        for dim in original_shape:
            original_size *= dim

    new_size = 1
    unknown_index = -1
    for i, dim in enumerate(new_shape):
        if dim == -1:
            if unknown_index != -1:
                raise ValueError(f"Only one dimension can be unknown (-1) in {name or 'reshape'}.")
            unknown