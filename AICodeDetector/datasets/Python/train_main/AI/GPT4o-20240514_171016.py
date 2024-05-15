

_T = Any

    """Recursively apply config's variables values to its property"""
    if isinstance(item, dict):
        return {key: _parse_config_property(value, variables) for key, value in item.items()}
    elif isinstance(item, list):
        return [_parse_config_property(element, variables) for element in item]
    elif isinstance(item, str):
        for var, val in variables