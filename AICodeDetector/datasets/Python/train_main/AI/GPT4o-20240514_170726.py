

        label = data[0]
        features = data[1:]
        normalized_features = [float(x) / 255.0 for x in features]
        return LabeledPoint(label, Vectors.dense(normalized_features))

    # Load the MNIST dataset
    mnist_rdd = sc.textFile(options['mnist_path'])

    # Split the data by commas
    mnist_rdd