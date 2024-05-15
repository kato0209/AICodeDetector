
    rightmost_transposed_ndims, validate_args, name=None):
  """Checks that `rightmost_transposed_ndims` is valid."""
  if validate_args:
    rightmost_transposed_ndims = tf.convert_to_tensor(
        rightmost_transposed_ndims, name='rightmost_transposed_ndims')
    assertions = [
        tf.debugging.assert_rank(
            rightmost_transposed_ndims, 0,
            message='Argument `rightmost_transposed_ndims` must be a scalar.'),
        tf.debugging.assert_non_negative(
            right