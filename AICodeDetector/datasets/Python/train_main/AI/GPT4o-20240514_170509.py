
class _PrettyDict(dict):
        return '{' + ', '.join(f'{k}: {v}' for k, v in self.items()) + '}'

    """Recursively replace `dict`s with `_PrettyDict`."""
    if isinstance(x, dict):
        return _PrettyDict({k: _recursively_replace_dict_for_pretty_dict(v) for k, v in x.items()})
    elif isinstance(x, list):
        return [_recursively_replace_dict_for_pretty_dict(i) for i in x]
