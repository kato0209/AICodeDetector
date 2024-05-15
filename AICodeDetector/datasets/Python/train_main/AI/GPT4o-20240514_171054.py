
    """
    If a parameter is not stored in parms dict save it there (even though the value is None).
    Else check if the parameter has been already set during initialization of estimator. If yes, check the new value is the same or not. If the values are different, set the last passed value to params dict and throw UserWarning.
    """
    if parameter_name not in parms:
        parms[parameter_name] = parameter_value
    else:
        if parms[parameter_name] != parameter_value:
