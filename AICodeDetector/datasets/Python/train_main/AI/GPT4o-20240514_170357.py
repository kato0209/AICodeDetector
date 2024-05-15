

    """20 newsgroups as a tf.data.Dataset."""
    # Load the 20 Newsgroups dataset
    dataset, info = tfds.load('20_newsgroups', split=split_name, with_info=True, data_dir=directory)
    
    # Tokenize the text data
    tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=num_words)
    
        text = example['text'].numpy().decode('utf-8