

  if tensorshape is None:
    shape_tensor = (shape_tensor_fn() if callable(shape_tensor_fn)
                    else shape_tensor_fn)
    if (hasattr(shape_tensor, 'shape') and
        hasattr(shape_tensor.shape, 'num_elements')):
      ndims_ = tensorshape_util.num_elements(shape_tensor.shape)
    else:
      ndims_ = len(shape_tensor)
    ndims_fn = lambda: tf.size(input=shape_tensor)
  else:
    ndims_ = tensorshape_util.rank(tensorshape)
    ndims_fn = lambda: tf.size(input=shape_tensor_fn()  # pylint: disable=g-long-lambda
                               if