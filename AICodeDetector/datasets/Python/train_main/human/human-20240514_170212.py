

  num_timesteps = tf.shape(input=time_series_tensor)[-1]

  # Compute the index of the first unmasked entry for each series in the batch.
  unmasked_negindices = (
      tf.cast(~broadcast_mask, tf.int32) *
      tf.range(num_timesteps, 0, -1))
  first_unmasked_indices = num_timesteps - tf.reduce_max(
      input_tensor=unmasked_negindices, axis=-1)

  if first_unmasked_indices.shape.ndims is None:
    raise NotImplementedError(
        'Cannot compute initial values of a masked time series with'
        'dynamic rank.')  # `batch_gather` requires static rank

  # Extract the initial value for each series in the batch.
  return tf.squeeze(tf.compat.v1.batch_gather(
      params=time_series_tensor,
      indices=first_unmasked_indices[..., tf.newaxis]), axis=-1)