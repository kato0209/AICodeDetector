

    """Builds fake data for unit testing."""
        features = {
            'feature1': tf.random.uniform([batch_size, 10]),
            'feature2': tf.random.uniform([batch_size, 5])
        }
        labels = tf.random.uniform([batch_size, 1], maxval=2, dtype=tf.int32)
        return features, labels

    return input_fn
