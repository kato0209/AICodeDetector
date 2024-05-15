

    url = "http://qwone.com/~jason/20Newsgroups/20news-18828.tar.gz"
    filename = os.path.join(source_dir, "20news-18828.tar.gz")
    
    if not os.path.exists(source_dir):
        os.makedirs(source_dir)
    
    if not os.path.exists(filename):
        urllib.request.urlretrieve(url, filename)
    
    with tarfile.open(filename, "r:gz") as tar:
