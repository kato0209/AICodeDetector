

    download_path = Path(download_path)
    if extract_paths is None:
        extract_paths = [download_path]
    elif isinstance(extract_paths, (str, Path)):
        extract_paths = [Path(extract_paths)]
    else:
        extract_paths = [Path(p) for p in extract_paths]

    # Ensure download directory exists
    download_path.mkdir(parents=True, exist_ok=True)
    
    # Download the file
   