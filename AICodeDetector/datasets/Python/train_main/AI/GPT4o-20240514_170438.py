

    """Get broadcast shape as a Python list of integers (preferred) or `Tensor`.

    Args:
        *tensors:  One or more `Tensor` objects (already converted!).

    Returns:
        broadcast shape:  Python list (if shapes determined statically), otherwise
        an `int32` `Tensor`.
    """
    shapes = [tf.shape(tensor) for tensor in tensors]
    broadcast_shape = tf.broadcast_static_shape(*[tensor.shape for tensor in tensors])
    
    if broadcast_shape.is_fully_defined():
        return