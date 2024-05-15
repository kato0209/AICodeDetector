

    """Convenience function which statically broadcasts shape when possible.

    Args:
        shape1:  `1-D` integer `Tensor`.  Already converted to tensor!
        shape2:  `1-D` integer `Tensor`.  Already converted to tensor!
        name:  A string name to prepend to created ops.

    Returns:
        The broadcast shape, either as `TensorShape` (if broadcast can be done
        statically), or as a `Tensor`.
    """
