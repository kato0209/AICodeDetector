
    if file_path is None:
        file_path = config["file_path"]
    if not os.path.exists(file_path):
        raise ValueError("File not found: {}".format(file_path))
    if not os.path.isfile(file_path):
        raise ValueError("File not found: {}".format(file_path))
    if batch_size <= 0:
        raise ValueError("Batch size must be positive")
    if batch_size > 1:
        raise ValueError("Batch size must be greater than 1")
    if batch_size < 0:
        raise ValueError("Batch size must