

    """Computes `log(sum(exp(input_tensor)))` along the specified axis."""
    max_input = np.max(input_tensor, axis=axis, keepdims=True)
    if keepdims:
        return np.log(np.sum(np.exp(input_tensor - max_input), axis=axis, keepdims=True)) + max_input
    else:
        return np.log(np.sum(np.exp(input_tensor - max_input), axis=axis)) + np.squeeze(max_input, axis=axis)
