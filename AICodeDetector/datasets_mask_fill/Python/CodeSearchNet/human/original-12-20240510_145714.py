
  for slices, overrides in slice_overrides_seq:
    dist = _apply_single_step(dist, params_event_ndims, slices, overrides)
  return dist