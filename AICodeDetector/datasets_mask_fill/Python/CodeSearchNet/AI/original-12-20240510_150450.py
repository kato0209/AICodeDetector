
    if name is None:
      name = params.name
    if not isinstance(params, (tuple, list)):
      params = [params]
    if len(params)!= num_components:
      raise ValueError("Length of params (%d) does not match length of"
                       " component_layer (%d)" % (len(params), num_components))
    self._distribution = distribution.Mixture(
        component_layer,
        params=params,
        validate_args=validate_args,
        name=name)

  def _batch_shape_tensor(self):
    return array_ops.shape(