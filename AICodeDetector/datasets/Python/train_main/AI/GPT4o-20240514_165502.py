
    """ function to check expected type and raise
    error if type is not correct """
    if not isinstance(value, expected_type):
        raise TypeError(f"Expected {expected_type} for key '{key}', but got {type(value)}.")
