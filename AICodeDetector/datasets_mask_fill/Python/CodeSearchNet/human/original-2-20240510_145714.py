
  dtype = tf.as_dtype(dtype)
  if hasattr(dtype, 'max'):
    return dtype.max
  use_finfo = is_floating(dtype) or is_complex(dtype)
  return np.finfo(dtype).max if use_finfo else np.iinfo(dtype).max