
  if isinstance(tensor_to_broadcast, list):
    return [_broadcast_to(t, t_tensor) for t_tensor in tensor_to_broadcast]
  else:
    return [_broadcast_to(t, t_tensor) for t_tensor in tensor_to_broadcast]


def _is_tensor(t):
  return isinstance(t, ops.Tensor) and t.op.type == "Const"


def _is_tensor_list(t):
  return isinstance(t, (list, tuple)) and _is_tensor(t[0])


