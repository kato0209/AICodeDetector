
    train_data = get_mnist(sc, "train", options.dataPath)\
        .map(lambda rec_tuple: (normalizer(rec_tuple[0], mnist.TRAIN_MEAN, mnist.TRAIN_STD),
                                rec_tuple[1]))\
        .map(lambda t: Sample.from_ndarray(t[0], t[1]))
    test_data = get_mnist(sc, "test", options.dataPath)\
        .map(lambda rec_tuple: (normalizer(rec_tuple[0], mnist.TEST_MEAN, mnist.TEST_STD),
                                rec_tuple[1]))\
        .map(lambda t: Sample.from_ndarray(t[0], t[1]))
 