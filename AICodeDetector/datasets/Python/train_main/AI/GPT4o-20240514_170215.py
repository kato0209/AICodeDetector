
    """Uses arg names to resolve distribution names."""
    resolved_names = {}
    for arg in dist_fn_args:
        if arg in dist_names:
            resolved_names[arg] = dist_names[arg]
        else:
            resolved_names[arg] = f"{leaf_name}_{arg}"
    return resolved_names
