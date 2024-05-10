
    with ops.name_scope(name, values=[num_components, component_params_size]):
      params_size = tensor_shape.TensorShape(
          [num_components, component_params_size])
      return array_ops.concat(
          0, [
              array_ops.shape(params_size)[:num_components],
              array_ops.expand_dims(params_size, -1)], 0)

  def _get_batch_shape(self):
    return array_ops.shape(self._mean())

  def _get_event_shape(self):
    return self._