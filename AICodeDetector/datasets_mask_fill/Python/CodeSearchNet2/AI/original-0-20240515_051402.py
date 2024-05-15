
  # TODO(josh11b): Implement `iter_next` in TensorFlow 2.x.
  shapes = nest.map_structure(lambda t: t.shape, tensors)
  if any([not shape.is_fully_defined() for shape in shapes]):
    # TODO(josh11b): If we can get a shape from a nested structure,
    # we can store it as a tensor of unknown shape.
    raise TypeError("Shapes must be fully defined")
  shape_list = [shape.as_list() for shape in shapes]
  if not shape_list:
    raise ValueError