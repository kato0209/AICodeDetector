
    """Returns opened file object for writing dialog logs.

    Returns:
        log_file: opened Python file object.
    """
    log_file_path = "dialog_logs.txt"
    log_file = open(log_file_path, "a")
    return log_file
