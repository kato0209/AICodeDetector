
  batch_shape_static = tensorshape_util.constant_value_as_shape(new_shape)
  if tensorshape_util.is_fully_defined(batch_shape_static):
    return np.int32(batch_shape_static), batch_shape_static, []
  with tf.name_scope(name or "calculate_reshape"):
    original_size = tf.reduce_prod(input_tensor=original_shape)
    implicit_dim = tf.equal(new_shape, -1)
    size_implicit_dim = (
        original_size // tf.maximum(1, -tf.reduce_prod(input_tensor=new_shape)))
    new_ndims = tf.shape(input=new_shape)
    expanded_new_shape = tf.where(  # Assumes exactly one `-1`.
        implicit_dim, tf.fill(new_ndims, size_implicit_dim), new_shape)
    validations = [] if not validate else [  # pylint: disable=g-long-ternary
        assert_util.assert_rank(
            original_shape, 1, message="Original shape must be a vector."),
       