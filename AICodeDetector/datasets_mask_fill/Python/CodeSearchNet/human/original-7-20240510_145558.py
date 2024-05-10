
    with tf.compat.v1.name_scope(name, 'CategoricalMixtureOfOneHotCategorical',
                                 [params, event_size, num_components]):
      dist = MixtureSameFamily.new(
          params,
          num_components,
          OneHotCategorical(
              event_size,
              validate_args=False,  # So we can eval on simplex interior.
           