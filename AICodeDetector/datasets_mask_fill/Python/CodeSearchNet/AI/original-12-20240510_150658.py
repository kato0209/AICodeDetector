 of the corresponding dense tensor.
    validate_args: `Boolean`, default `False`.  Whether to validate input
      with asserts.
    name: string, name of the operation.
    **kwargs: keyword arguments.

  Returns:
    A `Tensor` of shape `dense_a` and `dense_b`. Each of the matrices in `dense_a`
    are reduced together, one corresponding to the `SparseTensor` inputs of the
    resulting sum.

  Raises:
    ValueError: If `sparse_or_dense_a` and `dense_b` are not compatible.
    ValueError: If `sparse_