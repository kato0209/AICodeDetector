
  if a.dtype.base_dtype!= tf.float32:
    raise TypeError("Input matrix must be float32, got %s." % a.dtype)
  if a.get_shape().ndims is not None and a.get_shape().ndims < 2:
    raise ValueError(
        "Input matrix must be at least 2-dimensional. Found: %s" % a)
  if a.get_shape().ndims is not None and a.get_shape().ndims < 3:
    raise ValueError(
        "Input matrix must be at least 3-dimensional. Found: %s" % a