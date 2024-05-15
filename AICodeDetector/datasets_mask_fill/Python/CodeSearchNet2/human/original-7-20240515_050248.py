
  if tensorshape_util.rank(batch_shape.shape) is not None:
    if tensorshape_util.rank(batch_shape.shape) != 1:
      raise ValueError("`batch_shape` must be a vector "
                       "(saw rank: {}).".format(
                           tensorshape_util.rank(batch_shape.shape)))

  batch_shape_static = tensorshape_util.constant_value_as_shape(batch_shape)
  batch_size_static = tensorshape_util.num_elements(batch_shape_static)
  dist_batch_size_static = tensorshape_util.num_elements(
      distribution.batch_shape)

  if batch_size_static is not None and dist_batch_size_static is not None:
    if batch_size_static != dist_batch_size_static:
      raise ValueError("`batch_shape` size ({}) must match "
  