

    """Builds fake MNIST-style data for unit testing."""
        # Generate fake images (28x28 pixels, 1 channel)
        images = np.random.rand(batch_size, 28, 28, 1).astype(np.float32)
        # Generate fake labels (10 classes)
        labels = np.random.randint(0, 10, size=(batch_size,)).astype(np.int32)
        return images, labels

        dataset = tf.data.Dataset.from