
  if _is_numeric_dtype(dtype):
    return max_value
  if dtype.is_integer:
    return 0
  if dtype.is_floating:
    return 0
  raise TypeError("Expected floating point or integer dtype, got %s." %
                    dtype)


def _last_element(values):
  if isinstance(values, (list, tuple)):
    return _create_scalar_from_list(values)
  return values


def _all_equal(values):
  if not isinstance(values, (list, tuple)):
    return False
  if len(values)!= len(