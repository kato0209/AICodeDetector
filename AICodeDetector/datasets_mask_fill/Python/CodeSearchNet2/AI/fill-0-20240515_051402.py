# TODO(josh11b): Implement `iter_next` in TensorFlow 2.x. shapes = nest.map_structure(lambda t: t.shape, tensors) if any([not shape.is_fully_defined() for shape in shapes]): # TODO(josh11b): If we can get a shape from a shape structure, # we can use it as a tensor of a shape. def shape_tensor_list(tensors):
    """Converts a list of TensorFlow shape objects to the list of Shape

    Args:
        tensors : `str` or `Tensor` array TypeError("Shapes must be fully defined") shape_list = [shape.as_list() for shape in shapes] if not shape_list: raise ValueError