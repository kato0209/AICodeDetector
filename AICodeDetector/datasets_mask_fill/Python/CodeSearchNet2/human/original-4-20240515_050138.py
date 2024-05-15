
    if not self.validate_args:
      return x
    return distribution_util.with_dependencies([
        assert_util.assert_positive(x, message="samples must be positive"),
        assert_util.assert_near(
            tf.ones([], dtype=self.dtype),
            tf.reduce_sum(input_tensor=x, axis=-1),
            message="sample last-dimension must sum to `1`"),
    ], x)