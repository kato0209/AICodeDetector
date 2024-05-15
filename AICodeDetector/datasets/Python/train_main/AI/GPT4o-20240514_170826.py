

    sc = SparkContext.getOrCreate()
    
    # Load IMDB dataset
    (training_data, training_labels), (testing_data, testing_labels) = imdb.load_data(nb_words=5000)
    
    # Pad sequences to the same length
    max_len = 500
    training_data = np.array([np.pad(x, (0, max_len - len(x)), 'constant') for x in training_data])
    testing_data = np