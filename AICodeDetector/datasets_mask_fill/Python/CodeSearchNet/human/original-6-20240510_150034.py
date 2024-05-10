
    if isinstance(item, str):
        return item.format(**variables)
    elif isinstance(item, list):
        return [_parse_config_property(item, variables) for item in item]
    elif isinstance(item, dict):
        return {k: _parse_config_property(v, variables) for k, v in item.items()}
    else:
        return item