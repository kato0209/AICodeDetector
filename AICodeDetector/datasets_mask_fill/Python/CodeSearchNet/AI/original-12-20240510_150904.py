
    # Check if the file exists
    if not os.path.exists(path):
      raise Exception("File %s does not exist" % path)
    # Check if the file is a directory
    if os.path.isdir(path):
      files = os.listdir(path)
      if len(files) == 0:
        raise Exception("File %s is not empty" % path)
      elif len(files) > 1:
        raise Exception("File %s has multiple files" % path)
      else:
        return

    # Check if the file is a file
  