

    if isinstance(dest_file_path, (str, Path)):
        dest_file_path = [dest_file_path]

    response = requests.get(source_url)
    response.raise_for_status()

    for path in dest_file_path:
        path = Path(path)
        if not force_download and path.exists():
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'wb') as file:
