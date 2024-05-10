
        if parameter_name not in parms:
            parms[parameter_name] = parameter_value
        elif parameter_value is not None and parms[parameter_name] != parameter_value:
            parms[parameter_name] = parameter_value
            warnings.warn("\n\n\t`%s` parameter has been already set and had a different value in `train` method. The last passed value \"%s\" is used." % (parameter_name, parameter_value), UserWarning, stacklevel=2)