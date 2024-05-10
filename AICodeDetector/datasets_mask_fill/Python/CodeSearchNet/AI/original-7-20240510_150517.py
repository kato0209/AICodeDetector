
  with ops.name_scope(name, name_scope):
    mean_name = _convert_to_tensor(dist.mean().name)
    square_log_det = math_ops.log(dist.logits) - math_ops.log(2. * dist.probs)
    dist_log_det = math_ops.reduce_sum(square_log_det, axis=[-1])
    mean = array_ops.where(
        math_ops.greater(dist_log_det, 0.0),
        mean_name,
        array_ops.zeros_like