
    if override_shape is None:
      override_shape = []

    override_shape = tf.convert_to_tensor(
        value=override_shape, dtype=tf.int32, name=name)

    if not dtype_util.is_integer(override_shape.dtype):
      raise TypeError("shape override must be an integer")

    override_is_scalar = _is_scalar_from_shape_tensor(override_shape)
    if tf.get_static_value(override_is_scalar):
      return self._empty

    dynamic_assertions = []

    if tensorshape_util.rank(override_shape.shape) is not None:
      if tensorshape_util.rank(override_shape.shape) != 1:
        raise ValueError("shape override must be a vector")
    elif validate_args:
      dynamic_assertions += [
          assert_util.assert_rank(
