
  block_sizes_shape = block_sizes.shape
  if tensorshape_util.is_fully_defined(block_sizes_shape):
    if (tensorshape_util.rank(block_sizes_shape) != 1 or
        (tensorshape_util.num_elements(block_sizes_shape) != len(bijectors))):
      raise ValueError(
          '`block_sizes` must be `None`, or a vector of the same length as '
          '`bijectors`. Got a `Tensor` with shape {} and `bijectors` of '
          'length {}'.format(block_sizes_shape, len(bijectors)))
    return block_sizes
  elif validate_args:
    message = ('`block_sizes` must be `None`, or a vector of the same length '
               'as `bijectors`.')
