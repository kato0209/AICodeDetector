
    x_ndims = (
        tf.rank(x) if tensorshape_util.rank(x.shape) is None else
        tensorshape_util.rank(x.shape))
    event_ndims = (
        tf.size(input=self.event_shape_tensor())
        if tensorshape_util.rank(self.event_shape) is None else
        tensorshape_util.rank(self.event_shape))
    batch_ndims = (
        tf.size(input=self._batch_shape_unexpanded)
        if tensorshape_util.rank(self.batch_shape) is None else
        tensorshape_util.rank(self.batch_shape))
    sample_ndims = x_ndims - batch_ndims - event_ndims
    if isinstance(sample_ndims, int):
      static_sample_shape = x.shape[:sample_ndims]
    else:
    