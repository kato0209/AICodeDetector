
    with tf.compat.v1.name_scope(name, 'OneHotCategorical',
                                 [params, event_size]):
      return tfd.OneHotCategorical(
          logits=params,
          dtype=dtype or params.dtype.base_dtype,
          validate_args=validate_args)