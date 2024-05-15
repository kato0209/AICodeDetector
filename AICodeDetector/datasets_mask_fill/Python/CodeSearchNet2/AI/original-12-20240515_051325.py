
  with ops.name_scope(name, "kl_pareto_pareto", values=[a.logits, b.logits]):
    # Need to convert back to batched KL(a || b)
    batch_dims = a.batch_shape.ndims
    event_dims = b.event_shape.ndims
    if a.event_shape.ndims is not None and b.event_shape.ndims is not None:
      batch_dims = a.event_shape.ndims - b.event_shape.ndims
    if a.event_shape.ndims is not None and b.