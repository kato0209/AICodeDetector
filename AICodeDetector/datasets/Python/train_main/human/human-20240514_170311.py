
  output = tensor_to_broadcast
  for tensor in target_tensors:
    output += tf.zeros_like(tensor)
  return output