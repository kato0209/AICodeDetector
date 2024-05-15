

    signature = inspect.signature(f)
    valid_kwargs = {k: v for k, v in src_kwargs.items() if k in signature.parameters}
    return valid_kwargs
