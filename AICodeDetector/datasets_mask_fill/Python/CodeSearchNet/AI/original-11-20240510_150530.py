
  if not src_kwargs:
    return {}

  # Filter out keyword arguments that are not in the signature.
  filtered_kwargs = {k: v for k, v in src_kwargs.items() if k not in f.arg_names}

  # Filter out any kwargs that are in the signature.
  filtered_kwargs = {k: v for k, v in filtered_kwargs.items() if k in f.arg_names}

  # Filter out any keyword arguments that are in the signature.
  filtered_kwargs = {k: v for k, v in src_kwargs.items() if