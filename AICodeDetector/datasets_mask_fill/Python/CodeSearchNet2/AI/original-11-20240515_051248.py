
  with ops.name_scope(name, "vector_size_to_square_matrix_size",
                      values=[d]):
    if d.dtype.is_complex:
      raise TypeError("Input must be real-valued.")
    if d.dtype.is_floating:
      raise TypeError("Input must be real-valued, not complex.")
    d_shape = d.shape
    d_size = math_ops.cast(array_ops.shape(d), dtypes.float32)
    return array_ops.slice(array_ops.transpose(d, [1, 0, 2]),