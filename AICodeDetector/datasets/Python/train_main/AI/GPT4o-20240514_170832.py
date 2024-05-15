

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    filepath = os.path.join(data_dir, filename)
    if not os.path.exists(filepath):
        urllib.request.urlretrieve(url, filepath)
        with zipfile.ZipFile(filepath, 'r') as zip_ref:
            zip_ref.extractall(data_dir)

    url = 'http://files.grouplens.org/datasets/movielens/ml-