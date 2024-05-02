def creation_date(path_to_file):
    """
 <extra_id_0>  Try to get the date that a file was created, falling back to <extra_id_1> was
    last modified if <extra_id_2> possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
  <extra_id_3>     stat = os.stat(path_to_file)
  <extra_id_4>  <extra_id_5>  try:
            return stat.st_birthtime
        except AttributeError:
 <extra_id_6>        <extra_id_7> # We're probably on Linux. No easy way to <extra_id_8> dates