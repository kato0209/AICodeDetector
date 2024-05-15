
  assertions = []

  def validate_equal_last_dim(tensor_a, tensor_b, message):
    if tensor_a.shape.is_fully_defined() and tensor_b.shape.is_fully_defined():
      if tensor_a.shape[-1] != tensor_b.shape[-1]:
        raise ValueError(message)
    elif validate_args:
      assertions.append(
          tf.compat.v1.assert_equal(
              tf.shape(input=tensor_a)[-1],
              tf.shape(input=tensor_b)[-1],
              message=message))

  if logits is not None:
    validate_equal_last_dim(
        outcomes,
        logits,
    