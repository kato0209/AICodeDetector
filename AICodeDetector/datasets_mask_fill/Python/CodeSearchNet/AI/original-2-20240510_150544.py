

  def _input_fn():
    features = {
        'age':
            input_lib.limit_epochs(
                constant_op.constant([[.8], [.2], [.1]]),
                num_epochs=num_epochs),
        'language':
            sparse_tensor.SparseTensor(
                values=input_lib.limit_epochs(
                    ['en', 'fr', 'zh'], num_epochs=num_epochs),
     