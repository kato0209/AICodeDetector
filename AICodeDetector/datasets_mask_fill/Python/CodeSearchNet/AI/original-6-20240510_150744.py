
    if data_type == "train":
        data_url = "http://yann.lecun.com/exdb/mnist/"
        data_file = "mnist.pkl.gz"
    elif data_type == "test":
        data_url = "http://yann.lecun.com/exdb/mnist/"
        data_file = "mnist.pkl.gz"
    else:
        raise ValueError("data_type should be 'train' or 'test'")
    if not os.path.exists(location):
        os.makedirs(location)
    if data_type == "