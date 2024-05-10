
        if isinstance(keys, list):
            keys = keys[0]
        if isinstance(keys, str):
            keys = [keys]
        if not isinstance(keys, list):
            raise ValueError("keys must be a list")
        if not all([isinstance(k, str) for k in keys]):
            raise ValueError("keys must be a list of strings")
        if not all([isinstance(k, str) for k in keys]):
  