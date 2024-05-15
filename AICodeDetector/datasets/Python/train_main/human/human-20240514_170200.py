
  flat_values = []
  for value in values:
    # Checks if it is a namedtuple.
    if hasattr(value, '_fields'):
      for field in value._fields:
        flat_values.extend([field, _to_str(getattr(value, field))])
      continue
    if isinstance(value, (list, tuple)):
      for v in value:
        flat_values.append(_to_str(v))
      continue
    flat_values.append(_to_str(value))
  return tf.compat.v1.Print(pass_through_tensor, flat_values)