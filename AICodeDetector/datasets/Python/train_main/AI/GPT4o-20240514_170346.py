
    """Calls `fn`, appropriately reshaping its input `x` and output."""
    original_shape = x.shape
    x = x.reshape(-1, x.shape[-1])  # Flatten the input except for the last dimension

    if extra_kwargs is None:
        extra_kwargs = {}

    y = fn(x, **extra_kwargs)

    output_shape = list(original_shape)
    output_shape[-1] = y.shape[-1]
    y = y.reshape(output_shape)

    return y
