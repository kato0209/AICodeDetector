

    if not isinstance(from_structure, Iterable) or isinstance(from_structure, (str, bytes)):
        # If from_structure is a singleton, broadcast it to match to_structure
        if isinstance(to_structure, dict):
            return {k: from_structure for k in to_structure}
        elif isinstance(to_structure, (list, tuple)):
            return type(to_structure)(from_structure for _ in to_structure)
        else:
            return from_structure
    else:
        return from_structure
