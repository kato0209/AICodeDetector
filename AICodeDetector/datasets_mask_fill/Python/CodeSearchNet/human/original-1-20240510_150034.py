

    if isinstance(dest_file_path, list):
        dest_file_paths = [Path(path) for path in dest_file_path]
    else:
        dest_file_paths = [Path(dest_file_path).absolute()]

    if not force_download:
        to_check = list(dest_file_paths)
        dest_file_paths = []
        for p in to_check:
            if p.exists():
                log.info(f'File already exists in {p}')
            else:
           