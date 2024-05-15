

    processed_folder = 'path/to/processed_folder'
    url = 'http://path.to/emnist/data.gz'
    file_path = os.path.join(processed_folder, 'data.gz')

    if not os.path.exists(processed_folder):
        os.makedirs(processed_folder)

    if not os.path.exists(file_path):
        print("Downloading EMNIST data...")
        urllib.request.urlretrieve(url, file_path)
        print("Download complete.")

        with gzip.open(file_path, 'rb') as f_in:
            with open(os