

    """Stable evaluation of `Log[exp{big} - exp{small}]`.

    To work correctly, we should have the pointwise relation:  `small <= big`.

    Args:
        big: Floating-point `Tensor`
        small: Floating-point `Tensor` with same `dtype` as `big` and broadcastable
            shape.

    Returns:
        `Tensor` of same `dtype` of `big` and broadcast shape.
    """
    return big + tf.math.log1p(-tf.exp