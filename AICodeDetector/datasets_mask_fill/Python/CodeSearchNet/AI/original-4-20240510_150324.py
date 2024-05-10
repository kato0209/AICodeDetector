
    if operation is not None and parameters is not None:
        return operation, parameters
    return operation, parameters


def _literal_as_binds(element, name=None, type_=None):
    if hasattr(element, '__clause_element__'):
        return element.__clause_element__()
    elif not isinstance(element, Visitable):
        if element is None:
            return Null()
        else:
            return _BindParamClause(name, element, type_=type_, unique=True)
    else:
        return element


def _type_from_args(args):
    for a in args: