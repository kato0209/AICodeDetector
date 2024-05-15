if dtype is not None or not tf.nest.is_nested(struct): return tf.convert_to_tensor(struct, dtype=dtype) if _maybe_convertible_to_tensor(struct): try: # Try a nested conversion in the structure wholesale. return tf.convert_to_tensor(value=struct, name=name) except (ValueError, TypeError): # Unfortunately Eager/Graph /SparseTensor is still supported and don't take the value itself on the error type. if struct.ndim == 0: return 0
  return struct
else:
  return _extract_structure(struct)

def _nested_convert_to_tensor(struct, name):
  try: # Recursively convert the struct to a tensor, unless its not inside an array.
    return tf.convert_to_tensor(value=struct, dtype=struct.dtype, name=name)
  except (ValueError, TypeError): # Try converting all of its children. shallow_struct = _get_shallow_structure(struct) return nest.map_structure_up_to( shallow_struct, lambda s: _nested_convert_to_tensor(s, name=name), struct)