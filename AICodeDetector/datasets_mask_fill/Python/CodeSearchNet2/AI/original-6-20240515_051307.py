
    return tensor_shape.TensorShape(self._random_sample_shape)

  def _get_batch_shape(self):
    return common_shapes.broadcast_shape(
        self.total_count,
        self.batch_shape_tensor()[:-1])

  def _event_shape_tensor(self):
    return constant_op.constant([], dtype=dtypes.int32)

  def _get_event_shape(self):
    return tensor_shape.scalar()

  def _sample_n(self, n, seed=None):
    # Uniform variates must be sampled from the open