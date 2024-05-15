

    """
    Will test the filepath result and test if its size is at least self.filesize

    :param result: a list of dicts returned by Snakebite ls
    :param size: the file size in MB a file should be at least to trigger True
    :return: (bool) depending on the matching criteria
    """
    if size is None:
        return True
    
    size_in_bytes = size * 1024 * 1024
    
    for file_info in result:
        if 'length' in file_info and