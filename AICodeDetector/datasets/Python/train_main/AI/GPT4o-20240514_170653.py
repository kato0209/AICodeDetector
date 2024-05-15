

                           dense_b,
                           validate_args=False,
                           name=None,
                           **kwargs):
  """Returns (batched) matmul of a SparseTensor (or Tensor) with a Tensor."""
  with tf.name_scope(name or "sparse_or_dense_matmul"):
    if isinstance(sparse_or_dense_a, tf.SparseTensor):
      product = tf.sparse.sparse_dense_matmul(sparse_or_dense_a, dense_b, **kwargs)
    else:
      product = tf.matmul(sparse_or_dense_a, dense_b, **