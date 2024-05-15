
    # what is passed in json:
    config_params = {k: _resolve(v) for k, v in params.items()}

    # get component by reference (if any)
    if 'ref' in config_params:
        try:
            component = _refs[config_params['ref']]
            if serialized is not None:
                component.deserialize(serialized)
            return component
        except KeyError:
            e =