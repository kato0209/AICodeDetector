def creation_date(path_to_file):
   """
    Try to get the date that a file was created, falling back to when it was
   last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
      try:
   raise Exception('Could not get creation date.')

def modification_date(path_to_file):        return stat.st_birthtime
        except AttributeError:
 way         # We're probably on Linux. No way to get creation dates