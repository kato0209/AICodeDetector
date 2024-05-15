

    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest() == md5

    if not os.path.exists(root):
        os.makedirs(root)
    
    if filename is None:
        filename = os.path.basename(url)
    
    file