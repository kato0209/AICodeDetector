
    if source_dir is None:
        source_dir = os.path.join(os.path.dirname(__file__), "glove.6B")
    if not os.path.exists(source_dir):
        os.makedirs(source_dir)
    if not os.path.exists(os.path.join(source_dir, "glove.6B")):
        download(source_dir, "glove.6B")
    if not os.path.exists(os.path.join(source_dir, "glove.6B")):
        download(source_dir