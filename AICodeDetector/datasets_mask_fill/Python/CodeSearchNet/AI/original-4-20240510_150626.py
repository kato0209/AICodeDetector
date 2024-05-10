
  if (current_position is None or
      (current_position < 0 and current_objective < 0) or
      (current_position > 0 and current_objective > 0) or
      (current_position < 0 and current_objective == 0)):
    return True
  if (current_position < 0 or
      (current_position > 0 and current_objective < 0) or
      (current_position < 0 and current_objective > 0) or
      (current_position > 0 and current_objective == 0)):
    return True
  if (current_position < 0 or
      (current_position > 0