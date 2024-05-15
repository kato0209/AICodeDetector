
  if dtype and not dtype.is_compatible_with(struct.dtype):
    raise ValueError("Nested structures do not support "
                     "conversion between tf.Tensor and "
                     "tf.compat.v1.convert_to_tensor: %s" % struct)
  if isinstance(struct, tuple):
    return tuple(
        _nested_convert_to_tensor(substructure, dtype, name)
        for substructure in struct)
  elif isinstance(struct, dict):
    return _nested_convert_to_tensor(struct, dtype, name)
  elif isinstance(struct, tensor_array_