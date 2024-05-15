
    """Creates lists of callables suitable for JDSeq."""
    flattened = []
    for name, maker in named_makers:
        if isinstance(maker, list):
            flattened.extend(maker)
        else:
            flattened.append(maker)
    return flattened
