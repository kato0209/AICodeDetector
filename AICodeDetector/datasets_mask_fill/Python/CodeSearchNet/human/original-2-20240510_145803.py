
    dtype = util.maybe_get_common_dtype(
        [amplitude, length_scale])
    if amplitude is not None:
      amplitude = tf.convert_to_tensor(
          value=amplitude, name='amplitude', dtype=dtype)
    self._amplitude = _validate_arg_if_not_none(
        amplitude, tf.compat.v1.assert_positive, validate_args)
    if length_scale is not None:
      length_scale = tf.convert_to_tensor(
          value=length_scale, name='length_scale', dtype=dtype)
    self._length_scale = _validate_arg_if_not_none(
        length_scale, tf.compat.v1.assert_positive, validate_args)
    return dtype