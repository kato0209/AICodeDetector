
    w2v_dir = download_glove_w2v(source_dir)
    w2v_path = os.path.join(w2v_dir, "glove.6B.%sd.txt" % dim)
    if sys.version_info < (3,):
        w2v_f = open(w2v_path)
    else:
        w2v_f = open(w2v_path, encoding='latin-1')
    pre_w2v = {}
    for line in w2v_f.readlines():
        items = line.split(" ")
        pre_w2v[items[0]] = [float(i) for i in items[1:]]
    w2v_f.close()
    return pre_w2v