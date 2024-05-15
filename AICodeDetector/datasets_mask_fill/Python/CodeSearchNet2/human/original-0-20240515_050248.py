
  if dtype is not None or not tf.nest.is_nested(struct):
    return tf.convert_to_tensor(struct, dtype=dtype)

  if _maybe_convertible_to_tensor(struct):
    try:
      # Try converting the structure wholesale.
      return tf.convert_to_tensor(value=struct, name=name)
    except (ValueError, TypeError):
      # Unfortunately Eager/Graph mode don't agree on the error type.
      pass
  # Try converting all of its children.
  shallow_struct = _get_shallow_structure(struct)
  return nest.map_structure_up_to(
      shallow_struct, lambda s: _nested_convert_to_tensor(s, name=name), struct)