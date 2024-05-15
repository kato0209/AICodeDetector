
  if isinstance(target_log_prob, collections.Sequence):
    target_log_prob = [target_log_prob]
  if isinstance(target_log_prob, collections.Mapping):
    target_log_prob = collections.OrderedDict(target_log_prob)

  if isinstance(target_log_prob, collections.Sequence):
    target_log_prob = list(target_log_prob)

  if isinstance(target_log_prob, collections.Mapping):
    target_log_prob = collections.OrderedDict(target_log_prob)

  if isinstance(target_log_prob