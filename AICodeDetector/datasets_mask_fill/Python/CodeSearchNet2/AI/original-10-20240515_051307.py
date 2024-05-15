
    if old is None:
      return new
    elif isinstance(old, list):
      old = old[:]
      new = new[:]
    else:
      old = old.split(',')
      new = new.split(',')

    if len(old)!= len(new):
      raise ValueError('Cannot merge %s and %s' % (old, new))

    for i in range(len(old)):
      if old[i]!= new[i]:
        raise ValueError('Cannot merge %s and %s' % (old[i], new[i]))

    return new

  def _merge_dict(self,