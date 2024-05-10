
  if not isinstance(outcomes, ops.Tensor):
    raise TypeError("Expected outcomes to be a Tensor, got {}".format(type(outcomes)))
  if not isinstance(logits, ops.Tensor):
    raise TypeError("Expected logits to be a Tensor, got {}".format(type(logits)))
  if not isinstance(probs, ops.Tensor):
    raise TypeError("Expected probs to be a Tensor, got {}".format(type(probs)))
  if not probs.shape.is_compatible_with(probs.shape):
    raise TypeError("probs must have the same shape as logits, got {}"
                   .