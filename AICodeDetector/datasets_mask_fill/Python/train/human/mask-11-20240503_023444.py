def creation_date(path_to_file):
 <extra_id_0>  """
    Try to get the date that a <extra_id_1> created, falling back to when it was
 <extra_id_2>  last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
 <extra_id_3>    <extra_id_4> try:
   <extra_id_5>        return stat.st_birthtime
        except AttributeError:
 <extra_id_6>    <extra_id_7>     # We're probably on Linux. No <extra_id_8> to get creation dates