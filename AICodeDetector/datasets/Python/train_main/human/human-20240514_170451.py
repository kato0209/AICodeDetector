
  with tf.name_scope(name or 'maybe_validate_rightmost_transposed_ndims'):
    assertions = []
    if not dtype_util.is_integer(rightmost_transposed_ndims.dtype):
      raise TypeError('`rightmost_transposed_ndims` must be integer type.')

    if tensorshape_util.rank(rightmost_transposed_ndims.shape) is not None:
      if tensorshape_util.rank(rightmost_transposed_ndims.shape) != 0:
        raise ValueError('`rightmost_transposed_ndims` must be a scalar, '
                         'saw rank: {}.'.format(
                             tensorshape_util.rank(
            