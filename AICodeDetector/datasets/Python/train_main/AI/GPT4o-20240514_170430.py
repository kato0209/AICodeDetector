
    """Applies a sequence of slice or copy-with-overrides operations to `dist`."""
    for slice_overrides in slice_overrides_seq:
        if isinstance(slice_overrides, dict):
            dist = dist.copy(**slice_overrides)
        else:
            dist = dist[slice_overrides]
    return dist
