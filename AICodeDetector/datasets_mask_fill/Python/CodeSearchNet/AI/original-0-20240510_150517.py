
  # TODO(jamesmartens): consider adding a test for `time_series_tensor` once
  # it is implemented.
  time_series_tensor = ops.convert_to_tensor(time_series_tensor)
  time_series_tensor = array_ops.reshape(time_series_tensor, [-1])
  broadcast_mask = ops.convert_to_tensor(broadcast_mask)

  # TODO(jamesmartens): consider adding a test for `time_series_tensor` once
  # it is implemented.
  time_series_tensor = array_ops.where