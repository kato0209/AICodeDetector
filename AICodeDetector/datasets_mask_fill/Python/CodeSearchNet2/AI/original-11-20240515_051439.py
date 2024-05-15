
  for i, dim in enumerate(x.shape):
    if i in axis:
      raise ValueError('Cannot insert a loop dimension at a time with shape '
                       '%s for an innermost dimension.' % x.shape)
    if dim in (x.shape[0], 1):
      raise ValueError('Cannot insert a loop dimension at a time with shape '
                       '%s for an innermost dimension.' % x.shape)

  # Reverse the order of the dimensions so that we go from left