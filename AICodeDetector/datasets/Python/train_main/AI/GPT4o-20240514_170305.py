
    """Defers an operator overload to `attr`.

    Args:
        attr: Operator attribute to use.

    Returns:
        Function calling operator attribute.
    """
        return getattr(self, attr)(*args, **kwargs)
    return operator_func
