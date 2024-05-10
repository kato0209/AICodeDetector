
  samples = ops.convert_to_tensor(samples)
  event = ops.convert_to_tensor(event)
  samples = ops.convert_to_tensor(samples)
  event_ndims = ops.convert_to_tensor(event_ndims)

  # We do not know the rank of samples, so we need to broadcast
  # the samples.
  if event_ndims.shape.ndims is None:
    return samples, event

  # We can broadcast the samples.
  # This means we need to broadcast the event samples.
  # For simplicity, we use the fact that the rank of