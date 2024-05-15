
    """Helper which checks validity of `loc` and `scale` init args."""
    if validate_args:
        param = tf.convert_to_tensor(param, name=name)
        if param.dtype.is_floating:
            return param
        else:
            raise TypeError(f"{name} must be a floating point tensor.")
    return param
