
    # Load data
    (x_train, y_train), (x_test, y_test) = load_mnist(options.data_dir)

    # Split into training and test
    x_train = x_train.map(lambda x: x.split())
    x_test = x_test.map(lambda x: x.split())

    # Normalize
    x_train = preprocessing.scale(x_train)
    x_test = preprocessing.scale(x_test)

    # Split into training and test
    x_train = x_train.map(lambda x: x