
    """Make func to expand left/right (of axis) dims of tensors shaped like x."""
        shape = list(x.shape)
        for i in range(len(shape)):
            if i < axis:
                shape[i] = y_ref.shape[i]
            elif i > axis:
                shape[i] = y_ref.shape[i + 1]
        return x.reshape(shape)
    return expand_fn
