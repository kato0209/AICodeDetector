
    if isinstance(tensor, list):
        tensor = np.array(tensor)
    if tensor.ndim!= 3:
        raise ValueError('Tensor must be 3D')
    if tensor.shape[0]!= nrow * ncol:
        raise ValueError('Tensor must have shape (nrow, ncol)')
    if tensor.shape[1]!= nrow * ncol:
        raise ValueError('Tensor must have shape (nrow, ncol)')
    if normalize:
        tensor = tensor / np.max(tensor)
    if normalize:
        tensor = tensor / np.max(np.abs(tensor