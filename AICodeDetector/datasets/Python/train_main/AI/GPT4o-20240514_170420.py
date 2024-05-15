

    """Build fake MNIST-style data for unit testing."""
    # MNIST images are 28x28 pixels
    image_shape = (28, 28)
    # Generate random pixel values for images
    images = np.random.randint(0, 256, size=(num_examples, *image_shape), dtype=np.uint8)
    # Generate random labels (0-9) for each image
    labels = np.random.randint(0, 10, size=(num_examples,), dtype=np.uint8)
    return images, labels
