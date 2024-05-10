
  if isinstance(from_structure, type(to_structure)):
    if not nest.is_sequence(from_structure):
      raise TypeError("from_structure must be a sequence")
    # We allow changing the structure of the first structure to itself, as
    # this allows for consistent behavior across TensorFlow versions.
    new_from_structure = tuple(from_structure)
  else:
    new_from_structure = to_structure

  try:
    nest.assert_same_structure(from_structure, to_structure,
                               expand_composites=True)
  except (ValueError, TypeError) as e