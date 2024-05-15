
    if extract_paths is None:
        extract_paths = []

    if not os.path.isdir(download_path):
        os.makedirs(download_path)

    for path in extract_paths:
        if not os.path.exists(path):
            raise ValueError(f"Path {path} does not exist")

    if not os.path.isdir(download_path):
        raise ValueError(f"Download path {download_path} does not exist")

    if not os.path.exists(os.path.join(download_path, "extracted")):
        os.makedirs(os.