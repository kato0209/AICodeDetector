
    if not isinstance(value, expected_type):
        raise TypeError("{} argument must have a type {} not {}".format(
            key, expected_type, type(value)))