
    with tf.compat.v1.name_scope(
        name, 'CategoricalMixtureOfOneHotCategorical_params_size',
        [event_size, num_components]):
      return MixtureSameFamily.params_size(
          num_components,
          OneHotCategorical.params_size(event_size, name=name),
          name=name)