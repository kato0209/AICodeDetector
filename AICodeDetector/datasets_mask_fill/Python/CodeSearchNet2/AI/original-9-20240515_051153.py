
    if filename is None:
        filename = os.path.basename(url)
    if md5 is None:
        md5 = hashlib.md5()
    with open(filename, 'wb') as f:
        f.write(urllib2.urlopen(url).read())
    if root is not None:
        with open(filename, 'rb') as f:
            data = f.read()
        with open(filename, 'wb') as f:
            f.write(data)
        return md5.hexdigest()
    else:
      