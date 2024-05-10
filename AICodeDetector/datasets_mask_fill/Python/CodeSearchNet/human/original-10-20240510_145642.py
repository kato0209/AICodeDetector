
    if old is None:
      return new
    if new is None:
      return old
    if (old == new) if use_equals else (old is new):
      return old
    raise ValueError("Incompatible values: %s != %s" % (old, new))