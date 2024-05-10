
    if amplitude is None and length_scale is None:
      return None
    if amplitude is not None and length_scale is not None:
      raise ValueError("Cannot specify both `amplitude` and `length_scale` "
                       "at the same time.")
    if amplitude is not None and length_scale is None:
      raise ValueError("Cannot specify both `amplitude` and `length_scale` "
                       "at the same time.")
    if amplitude is