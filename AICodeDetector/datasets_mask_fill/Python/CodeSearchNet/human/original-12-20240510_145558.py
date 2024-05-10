
    with tf.compat.v1.name_scope(name, 'MixtureSameFamily',
                                 [params, num_components, component_layer]):
      params = tf.convert_to_tensor(value=params, name='params')
      num_components = tf.convert_to_tensor(
          value=num_components, name='num_components', dtype_hint=tf.int32)

      components_dist = component_layer(
          tf.reshape(
              params[..., num_components:],
              tf.concat([tf.shape(input=params)[:-1], [num_components, -1]],
        