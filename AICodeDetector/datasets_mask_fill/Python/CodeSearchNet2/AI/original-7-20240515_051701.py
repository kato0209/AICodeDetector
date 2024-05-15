
    if serialized is None:
        serialized = {}
    if mode == 'infer':
        return Component(params, serialized)
    elif mode == 'export':
        return Component(params, serialized, **kwargs)
    elif mode == 'export_tf':
        return Component(params, serialized, **kwargs)
    elif mode == 'export_tf_with_metadata':
        return Component(params, serialized, **kwargs)
    elif mode == 'export_tf_with_metadata_with_metadata':
        return Component(params, serialized, **kwargs)
    elif mode == 'export_tf_with_metadata_