
    if not self._inbound_nodes:
      raise ValueError('The layer has never been called '
                       'and thus has no defined input shape.')
    all_input_shapes = set(
        [str(node.input_shapes) for node in self._inbound_nodes])
    if len(all_input_shapes) == 1:
      output_shape = self._inbound_nodes[0].output_shapes
      if isinstance(output_shape, list):
        return [tensor_shape.TensorShape(shape) for shape in output_shape]
      else:
        return [tensor_shape.TensorShape(output