
    input_shape = tf.TensorShape(input_shape)
    input_shape = input_shape.with_rank_at_least(2)
    if tf.compat.dimension_value(input_shape[-1]) is None:
      raise ValueError(
          'The innermost dimension of `input_shape` must be defined, '
          'but saw: {}'.format(input_shape))
    return input_shape[:-1].concatenate(self.units)