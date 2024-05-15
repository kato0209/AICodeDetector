
    """Shared init logic for `amplitude` and `length_scale` params.

    Args:
      amplitude: `Tensor` (or convertible) or `None` to convert, validate.
      length_scale: `Tensor` (or convertible) or `None` to convert, validate.
      validate_args: If `True`, parameters are checked for validity despite
        possibly degrading runtime performance

    Returns:
      dtype: The common `DType` of the parameters.
    """
    if amplitude is not None:
        amplitude = tf.convert_to