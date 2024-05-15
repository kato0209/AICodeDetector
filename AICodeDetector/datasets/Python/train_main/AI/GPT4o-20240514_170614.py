

    """
    Build fake CIFAR10-style data for unit testing.
    
    Parameters:
    - num_samples: Number of samples to generate.
    - image_size: Size of each image (height, width, channels).
    - num_classes: Number of classes.
    
    Returns:
    - X: NumPy array of shape (num_samples, height, width, channels) containing the fake images.
    - y: NumPy array of shape (num_samples,)